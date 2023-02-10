#(©)Codexbotz
#This Code is heavily modified for heaven exclusively By TargetX25 So he deserve a big piece of credits too.

from pyrogram import Client, filters
from pyrogram.types import Message
from bot import Bot
from config import ADMINS
from helper_func import encode, get_message_id, get_message_mg
from utils import get_shortlink
from temp import get_size

@Bot.on_message(filters.private & filters.user(ADMINS) & filters.command('series'))
async def series(client: Client, message: Message):
    while True:
        try:
            ek_message = await client.ask(text = "Forward the First 480P Ep. Post from Database channel WITH Tag<b/>", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        ek_msg_id = await get_message_id(client, ek_message)
        if ek_msg_id:
            break
        else:
            await ek_message.reply("❌ Error\n\nthis Forwarded Post is not from my DB Channel or this Link is taken from DB Channel", quote = True)
            continue

    while True:
        try:
            do_message = await client.ask(text = "Forward the Last 480P Ep. Post from Database channel WITH Tag", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        do_msg_id = await get_message_id(client, do_message)
        if do_msg_id:
            break
        else:
            await do_message.reply("❌ Error\n\nthis Forwarded Post is not from my DB Channel or this Link is taken from DB Channel", quote = True)
            continue
    
    while True:
        try:
            teen_message = await client.ask(text = "Forward the First 720P Ep. Post from Database channel WITH Tag", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        teen_msg_id = await get_message_id(client, teen_message)
        if teen_msg_id:
            break
        else:
            await teen_message.reply("❌ Error\n\nthis Forwarded Post is not from my DB Channel or this Link is taken from DB Channel", quote = True)
            continue
    
    while True:
        try:
            char_message = await client.ask(text = "Forward the Last 720P Ep. Post from Database channel WITH Tag", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        char_msg_id = await get_message_id(client, char_message)
        if char_msg_id:
            break
        else:
            await char_message.reply("❌ Error\n\nthis Forwarded Post is not from my DB Channel or this Link is taken from DB Channel", quote = True)
            continue
    
    while True:
        try:
            panch_message = await client.ask(text = "Forward the Series NAME with other details from Database channel WITH Tag", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        panch_msg_id = await get_message_mg(client, panch_message)
        if panch_msg_id:
            break
        else:
            await panch_message.reply("❌ Error\n\nthis Forwarded Post is not from my DB Channel or this Link is not taken from DB Channel", quote = True)
            continue
    
    while True:
        try:
            che_message = await client.ask(text = "Forward the Series POSTER from Database channel WITH Tag", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        che_msg_id = await get_message_mg(client, che_message)
        if che_msg_id:
            break
        else:
            await che_message.reply("❌ Error\n\nthis Forwarded Post is not from my DB Channel or this Link is not taken from DB Channel", quote = True)
            continue



    ek_string = f"get-{ek_msg_id * abs(client.db_channel.id)}-{do_msg_id * abs(client.db_channel.id)}"
    ek_base64_string = await encode(ek_string)
    ek_link =  await get_shortlink(f"https://telegram.me/{client.username}?start={ek_base64_string}")
    do_string = f"get-{teen_msg_id * abs(client.db_channel.id)}-{char_msg_id * abs(client.db_channel.id)}"
    do_base64_string = await encode(do_string)
    do_link =  await get_shortlink(f"https://telegram.me/{client.username}?start={do_base64_string}")
    media_ek = ek_message.video
    ek_size = get_size(media_ek.file_size)
    media_do = teen_message.video
    do_size = get_size(media_do.file_size)
    await che_message.reply_text(f"<a href='{che_msg_id}'>🎬</a> 𝐓𝐢𝐭𝐥𝐞: <b>{panch_msg_id}</b>\n🔊 𝐋𝐚𝐧𝐠𝐮𝐚𝐠𝐞: <b>English & Hindi</b>\n🎞 𝐐𝐮𝐚𝐥𝐢𝐭𝐲: <b>WEBRip</b>\n📧 𝐒𝐮𝐛𝐭𝐢𝐭𝐥𝐞𝐬: <b>Esubs</b>\n<b>〰〰〰〰〰〰〰〰〰〰〰\n🧑‍💻How to Download :\nWatch </b>👉\n<b>https://t.me/HeavenForYouAll/7878</b>\n<b>〰〰〰〰〰〰〰〰〰〰〰\n\n480p x264 [Around {ek_size} per Episode]\n👉{ek_link}\n\n720p x264 [Around {do_size} per Episode]\n👉{do_link}\n\n.........................................................\n🎯 Join : </b><b>@HeavenForYouAll</b>\n<b>---------------------------------------------</b>\n", quote=True)
 
@Bot.on_message(filters.private & filters.user(ADMINS) & filters.command('single'))
async def single(client: Client, message: Message):
    while True:
        try:
            first_message = await client.ask(text = "Forward the First Ep. Post from Database channel WITH Tag", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        f_msg_id = await get_message_id(client, first_message)
        if f_msg_id:
            break
        else:
            await first_message.reply("❌ Error\n\nthis Forwarded Post is not from my DB Channel or this Link is taken from DB Channel", quote = True)
            continue

    while True:
        try:
            second_message = await client.ask(text = "Forward the Last Ep. Post from Database channel WITH Tag", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        s_msg_id = await get_message_id(client, second_message)
        if s_msg_id:
            break
        else:
            await second_message.reply("❌ Error\n\nthis Forwarded Post is not from my DB Channel or this Link is taken from DB Channel", quote = True)
            continue


    string = f"get-{f_msg_id * abs(client.db_channel.id)}-{s_msg_id * abs(client.db_channel.id)}"
    base64_string = await encode(string)
    link =  await get_shortlink(f"https://telegram.me/{client.username}?start={base64_string}")
    await second_message.reply_text(f"<b>Here is your link</b>\n\n{link}", quote=True)



@Bot.on_message(filters.private & filters.user(ADMINS) & filters.command('movie'))
async def movie(client: Client, message: Message):
    while True:
        try:
            pehla_message = await client.ask(text = "Forward 480P File Post from Database channel WITH Tag", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        first_msg_id = await get_message_id(client, pehla_message)
        if first_msg_id:
            break
        else:
            await pehla_message.reply("❌ Error\n\nthis Forwarded Post is not from my DB Channel or this Link is not taken from DB Channel", quote = True)
            continue
            
            
    while True:
        try:
            dusra_message = await client.ask(text = "Forward 720P HEVC File Post from Database channel WITH Tag", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        second_msg_id = await get_message_id(client, dusra_message)
        if second_msg_id:
            break
        else:
            await dusra_message.reply("❌ Error\n\nthis Forwarded Post is not from my DB Channel or this Link is not taken from DB Channel", quote = True)
            continue
     
    while True:
        try:
            tesra_message = await client.ask(text = "Forward 720P File Post from Database channel WITH Tag", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        third_msg_id = await get_message_id(client, tesra_message)
        if third_msg_id:
            break
        else:
            await tesra_message.reply("❌ Error\n\nthis Forwarded Post is not from my DB Channel or this Link is not taken from DB Channel", quote = True)
            continue
    
    while True:
        try:
            chautha_message = await client.ask(text = "Forward 1080P File Post from Database channel WITH Tag", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        fourth_msg_id = await get_message_id(client, chautha_message)
        if fourth_msg_id:
            break
        else:
            await chautha_message.reply("❌ Error\n\nthis Forwarded Post is not from my DB Channel or this Link is not taken from DB Channel", quote = True) 
            continue
            
    while True:
        try:
            panchma_message = await client.ask(text = "Forward Movie Name Post from Database channel WITH Tage", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        fifth_msg_id = await get_message_mg(client, panchma_message)
        if fifth_msg_id:
            break
        else:
            await panchma_message.reply("❌ Error\n\nthis Forwarded Post is not from my DB Channel or this Link is not taken from DB Channel", quote = True)
            continue
    
    while True:
        try:
            chatha_message = await client.ask(text = "Forward POSTER Link Post from Database channel WITH Tag", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        sixth_msg_id = await get_message_mg(client, chatha_message)
        if sixth_msg_id:
            break
        else:
            await chatha_message.reply("❌ Error\n\nthis Forwarded Post is not from my DB Channel or this Link is not taken from DB Channel", quote = True)
            continue

    first_base64_string = await encode(f"get-{first_msg_id * abs(client.db_channel.id)}")
    first_link = await get_shortlink(f"https://telegram.me/{client.username}?start={first_base64_string}")
    second_base64_string = await encode(f"get-{second_msg_id * abs(client.db_channel.id)}")
    second_link = await get_shortlink(f"https://telegram.me/{client.username}?start={second_base64_string}")
    third_base64_string = await encode(f"get-{third_msg_id * abs(client.db_channel.id)}")
    third_link = await get_shortlink(f"https://telegram.me/{client.username}?start={third_base64_string}")
    fourth_base64_string = await encode(f"get-{fourth_msg_id * abs(client.db_channel.id)}")
    fourth_link = await get_shortlink(f"https://telegram.me/{client.username}?start={fourth_base64_string}")
    media_one = pehla_message.video
    first_size = get_size(media_one.file_size)
    media_two = dusra_message.video
    second_size = get_size(media_two.file_size)
    media_three = tesra_message.video
    third_size = get_size(media_three.file_size)
    media_four = chautha_message.video
    fourth_size = get_size(media_four.file_size)
    await chatha_message.reply_text(f"<a href='{sixth_msg_id}'>🎬</a> 𝐓𝐢𝐭𝐥𝐞: <b>{fifth_msg_id}</b>\n🔊 𝐋𝐚𝐧𝐠𝐮𝐚𝐠𝐞: <b>English & Hindi</b>\n🎞 𝐐𝐮𝐚𝐥𝐢𝐭𝐲: <b>WEBRip</b>\n📧 𝐒𝐮𝐛𝐭𝐢𝐭𝐥𝐞𝐬: <b>Esubs</b>\n<b>〰〰〰〰〰〰〰〰〰〰〰\n🧑‍💻How to Download :\nWatch </b>👉\n<b>https://t.me/HeavenForYouAll/7878</b>\n<b>〰〰〰〰〰〰〰〰〰〰〰\n\n480p x264 [{first_size}]\n👉{first_link}\n\n720p x265 [{second_size}]\n👉{second_link}\n\n720p x264 [{third_size}]\n👉{third_link}\n\n1080p x264 [{fourth_size}]\n👉{fourth_link}\n\n.........................................................\n🎯 Join : </b><b>@HeavenForYouAll</b>\n<b>---------------------------------------------</b>\n", quote=True)
