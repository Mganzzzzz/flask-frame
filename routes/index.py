from routes import *
import redis

main = Blueprint('index', __name__)

# Model = User
red = redis.Redis(host='qc.mganz.cc', port=6379, db=1)
print('redis', red)
chat_channel = 'chat'

def foo(number):
    return number


def stream():
    '''
    监听 redis 广播并 sse 到客户端
    '''
    # 对每一个用户 创建一个[发布订阅]对象
    pubsub = red.pubsub()
    # 订阅广播频道
    pubsub.subscribe(chat_channel)
    # 监听订阅的广播
    for message in pubsub.listen():
        print('message', message)
        if message['type'] == 'message':
            data = message['data'].decode('utf-8')
            # 用 sse 返回给前端
            yield 'data: {}\n\n'.format(data)


@main.route('/subscribe')
def subscribe():
    return Response(stream(), mimetype="text/event-stream")


@main.route('/')
@login_required
def index():
    return render_template('index.html')


@main.route('/test')
def fn():
    # return redirect(url_for('.fn1'))
    return redirect('/redirect/123')

@main.route('/redirect/<int:id>')
def fn1(id):
    print('id', id)
    return render_template('fn.html', id=id)


def current_time():
    return int(time.time())


@main.route('/chat/add', methods=['POST'])
@login_required
def chat_add():
    msg = request.get_json()
    print('msg', msg)
    # name = msg.get('name', '')
    u = current_user()
    content = msg.get('content', '')
    content = content.replace("<", "&lt;")
    content = content.replace(">", "&gt;")
    channel = msg.get('channel', '')
    form = {
        'user_id': u.id,
    }
    r = {
        'name': u.username,
        'avatar': u.avatar,
        'content': content,
        'channel': channel,
        'created_time': current_time(),
    }
    form.update(r)
    chat = Chat(form)
    chatValid = chat.valid()
    print('chatValid', chatValid)
    if chatValid:
        chat.save()
        message = json.dumps(r, ensure_ascii=False)
        print('debug', message)
        # 用 redis 发布消息
        red.publish(chat_channel, message)
        return 'OK'
    else:
        abort(410)
