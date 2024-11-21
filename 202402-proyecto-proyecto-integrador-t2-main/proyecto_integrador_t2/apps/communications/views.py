from django.shortcuts import redirect, render
from apps.accounts.models import Userk
from .models import Chat, Message
from django.db.models import Subquery, OuterRef
from .forms import ChatMessageCreateForm
from django.contrib.auth.decorators import login_required
from apps.accounts.decorators import allowed_users
# Create your views here.

#CLIENT------------------------------------------------------------------------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['client'])
def clientMessageHome(request):
    latest_message = Message.objects.filter(chat=OuterRef('pk')).order_by('-timeCreated').values('timeCreated')[:1]

    chats = request.user.client.chat.annotate(last_message_time=Subquery(latest_message)).order_by('-last_message_time')

    latestChat = chats.first()

    context = {
        'chats': chats, 
        'latestChat' : latestChat
    }
    
    return render(request, 'communications/clientMessageHome.html', context)



@login_required(login_url='login')
@allowed_users(allowed_roles=['client'])
def clientMessage(request, chatName):
    latest_message = Message.objects.filter(chat=OuterRef('pk')).order_by('-timeCreated').values('timeCreated')[:1]
  
    chats = request.user.client.chat.annotate(last_message_time=Subquery(latest_message)).order_by('-last_message_time')

    chat = Chat.objects.get(chatName = chatName)
    chatMessages = chat.chatMessages.all().order_by('timeCreated')[:30]
    
    form = ChatMessageCreateForm()
    if request.method == 'POST':
        form = ChatMessageCreateForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.author = request.user
            message.chat = chat
            message.save()
            # Redirigir a la misma página para evitar reenvíos del formulario
            return redirect('clientMessage', chatName=chatName)

    context = {
        'chat' : chat,
        'chatMessages' : chatMessages,
        'chats': chats,
        'form' : form,
        'chatName' : chatName
    }
    return render(request, 'communications/clientMessage.html', context)



@login_required(login_url='login')
@allowed_users(allowed_roles=['client'])
def clientCreateComprobateChat(request, username):
    if request.user.username == username:
        return redirect('clientMessageHome')

    otherUser = Userk.objects.get(username = username)
    freelancer = otherUser.freelancer

    chats = request.user.client.chat.all()

    chat = None
    if chats.exists():
        for chat_instance in chats:
            if freelancer==chat_instance.freelancer:
                chat = chat_instance
                break
        if not chat:
            chat = Chat.objects.create(freelancer=freelancer, client=request.user.client)
    else:
        chat = Chat.objects.create(freelancer=freelancer, client=request.user.client)
    
    chatName = chat.chatName

    return redirect('clientMessage', chatName)

#FREELANCER------------------------------------------------------------------------------
@login_required(login_url='login')
@allowed_users(allowed_roles=['freelancer'])
def freelancerMessageHome(request):

    latest_message = Message.objects.filter(chat=OuterRef('pk')).order_by('-timeCreated').values('timeCreated')[:1]


    chats = request.user.freelancer.chat.annotate(last_message_time=Subquery(latest_message)).order_by('-last_message_time')

    latestChat = chats.first()

    context = {
        'chats': chats, 
        'latestChat' : latestChat
    }
    return render(request, 'communications/freelancerMessageHome.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['freelancer'])
def freelancerMessage(request, chatName):
    latest_message = Message.objects.filter(chat=OuterRef('pk')).order_by('-timeCreated').values('timeCreated')[:1]

    # Obtención de todos los chats asociados al freelancer
    chats = request.user.freelancer.chat.annotate(last_message_time=Subquery(latest_message)).order_by('-last_message_time')

    # Obtención del chat actual y sus mensajes
    chat = Chat.objects.get(chatName=chatName)
    chatMessages = chat.chatMessages.all().order_by('timeCreated')[:30]
    lastMessage = chatMessages.first()

    # Inicializar formulario
    form = ChatMessageCreateForm()

    # Procesar envío del formulario mediante método POST
    if request.method == "POST":
        form = ChatMessageCreateForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.author = request.user
            message.chat = chat
            message.save()
            # Recargar la lista de mensajes después de guardar
            chatMessages = chat.chatMessages.all().order_by('timeCreated')[:30]

    context = {
        'chat': chat,
        'chatMessages': chatMessages,
        'chats': chats,
        'form': form,
        'chatName': chatName,
        'lastMessage': lastMessage,
    }
    return render(request, 'communications/freelancerMessage.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['freelancer'])
def freelancerCreateComprobateChat(request, username):
    if request.user.username == username:
        return redirect('freelancerMessageHome')

    otherUser = Userk.objects.get(username = username)
    client = otherUser.client

    chats = request.user.freelancer.chat.all()

    chat = None
    if chats.exists():
        for chat_instance in chats:
            if client==chat_instance.client:
                chat = chat_instance
                break
        if not chat:
            chat = Chat.objects.create(client=client, freelancer=request.user.freelancer)
    else:
        chat = Chat.objects.create(client=client, freelancer=request.user.freelancer)
    
    chatName = chat.chatName

    return redirect('freelancerMessage', chatName)

