'''我的主页'''
import streamlit as st
from PIL import Image
import time

# 进度条st.progress()
roading = st.progress(0, '开始加载')
for i in range(1, 101, 1):
    time.sleep(0.02)
    roading.progress(i, '正在加载'+str(i)+'%')
roading.progress(100, '加载完毕！')

page = st.sidebar.radio('我的首页', ['💭日常分享', '🔍实用的小工具','📽️影片推荐','📥留言区','💻其他网站'])
st.snow()

def page_1():
    '''日常分享'''
    #with open('编程猫的梦想.mp3', 'rb') as f:
        #mymp3 = f.read()
    #st.audio(mymp3, format='audio/mp3', start_time=0)
    tab5, tab6, tab7, tab8 = st.tabs(["📖学习","🍽️美食","🌎风景","📝文字感受"])
    with tab5:
        st.write('♡study')
        st.write('1.道法感悟')
        st.image('daofa.png')
        st.write('2.语文笔记')
        st.image('note1.png')
        st.image('note2.png')
        st.image('note3.png')
    with tab6:
        st.write('♡food')
        st.image('food1.jpg')
    with tab7:
        st.write('♡scenery')
        st.image('sun.jpg')
    with tab8:
        st.write('♡write it down')
        st.write('暂时还没有内容哦 敬请期待')
            
def page_2():
    '''实用的小工具'''
    st.write('这里有一些小工具 希望能够帮到你*≧▽≦')  
    # 图片处理工具
    st.write('☆图片处理工具☆')
    st.write('Tip:此工具可以帮助你处理图片')
    uploaded_file = st.file_uploader("上传图片", type=['png', 'jpeg', 'jpg'])
    if uploaded_file:
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        tab1,tab2,tab3,tab4 = st.tabs(["原图","改色1","改色2","改色3"])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img, 0, 2, 1))
        with tab3:
            st.image(img_change(img, 1, 2, 0))
        with tab4:
            st.image(img_change(img, 1, 0, 2))
    st.write('-----------------------------')
    # 智慧词典        
    st.write('☆智慧词典☆')
    st.write('Tip:此工具可以帮助你查询单词')
    with open('words_space.txt', 'r', encoding='utf-8') as f:
        words_list = f.read().split('\n')
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] =  [int(i[0]), i[2]]
    with  open('check_out_times.txt', 'r', encoding='utf-8') as f:
        times_list = f.read().split()
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')
    times_dict = {}
    for i in times_list:
        times_dict[i[0]] =  int(i[1])
    word = st.text_input('请输入要查询的单词')
    if word in words_dict:
        st.write(words_dict[word])
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        with open('check_out_times.txt', 'w', encoding='utf-8') as f:
            message = ''
            for k, v in times_dict.items():
                message += str(k) + '#' + str(v) + '\n'
            message = message[:-1]
            f.write(message)
        st.write('查询次数:', times_dict[n])
        
def page_3():
    '''影片推荐'''
    st.write('Tip：推荐的影片数据均来源于网络 排名不分先后 该模块将持续更新噢 ')
    tab9,tab10,tab11 = st.tabs(["《觉醒年代》","《万里归途》","个性化推荐电影"])
    with tab9:
        st.write('📌简要介绍：电视剧《觉醒年代》以1915年《青年杂志》问世到1921年《新青年》成为中国共产党机关刊物为贯穿，展现了从新文化运动、五四运动到中国共产党建立这段波澜壮阔的历史画卷，讲述了觉醒年代社会风情和百态人生。')
        st.write('📌该剧以李大钊、陈独秀、胡适从相识、相知到分手，走上不同人生道路的传奇故事为基本叙事线，以毛泽东、周恩来、陈延年、陈乔年、邓中夏、赵世炎等革命青年追求真理的坎坷经历为辅助线，艺术地再现了一百年前中国的先进分子和一群热血青年演绎出的一段追求真理、燃烧理想的澎湃岁月，深刻地揭示了马克思主义与中国工人运动相结合和中国共产党建立的历史必然性。')
        st.write('📌豆瓣评分：9.3（数据来源于网络）')
        st.video('觉醒年代.mp4')
    with tab10:
        st.write('📌简要介绍：《万里归途》讲述努米亚共 和国发生暴乱，撤侨行动刻不容缓。由于使馆人手不够，原本只是协助撤侨工作的外交官宗大伟和新人成朗临危受命，主动放弃回家机会，支援撤侨行动，他们逆行深入战区，营救被困同胞。')
        st.write('📌《万里归途》作为新时代主旋律电影，首次聚磨笑亩焦中国外交官撤侨背后的故事，以小人物见证大时代，有着潜移默化的影升此响力、润物无声的感染力。它以振奋人心的事例、宏大瞎森的战争场面直接触及人的内心情感传扬了中国精神。')
        st.write('📌豆瓣评分：7.2（数据来源于网络）')
        st.video('万里归途.mp4')
    with tab11:
        st.write('Tip：选出你最喜欢的电影类型 会为你推荐电影哦')
        st.write('请耐心等待~')
        st.write('----')
        st.write('你最喜欢的电影类型（单选）')
        cb1 = st.checkbox('动作、冒险')
        cb2 = st.checkbox('悬疑、惊悚')
        cb3 = st.checkbox('家庭、伦理')
        cb4 = st.checkbox('记录、历史')
        cb5 = st.checkbox('青春、励志')
        l = [cb1]
        a = [cb2]
        b = [cb3]
        c = [cb4]
        d = [cb5]
        if st.button('确认答案'):
            if True in l:
                st.write('为你推荐《速度与激情》')
            elif True in a:
                st.write('为你推荐《盗梦空间》')
            elif True in b:
                st.write('为你推荐《相助》')
            elif True in c:
                st.write('为你推荐《辛德勒的名单》')
            elif True in d:
                st.write('为你推荐《阿甘正传》')
        
def page_4():
    '''留言区'''
    st.write('Tip:你的意见或想法可以留在这里 Thanks♪(･ω･)ﾉ')
    with open('leave_messages.txt', 'r', encoding='utf-8') as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    for i in messages_list:
        if i[1] == '阿短':
            with st.chat_message('🌟'):
                st.write(i[1], ':', i[2])
        elif i[1] == '编程猫':
            with st.chat_message('🌊'):
                st.write(i[1], ':', i[2])
    name = st.selectbox('我是……', ['阿短', '编程猫'])
    new_message = st.text_input('想要说的话……')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1), name, new_message])
        with open('leave_messages.txt', 'w', encoding='utf-8') as f:
            message = ''
            for i in messages_list:
                message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
            message = message[:-1]
            f.write(message)
            
def img_change(img, rc, gc, bc):
    '''图片处理'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x, y][rc]
            g = img_array[x, y][gc]
            b = img_array[x, y][bc]
            img_array[x, y] = (b, g, r)
    return img

def page_5():
    '''其他网站'''
    st.write('除了本主站之外，我还将我的有趣内容分享在了其他网站中')
    go = st.selectbox('你的支持是我最大的动力，去支持一下up吧！', ['我的贴吧', '我的bilibili'])
    if go == '我的贴吧':
        st.link_button('帮我盖楼', 'https://www.baidu.com/')
    elif go == '我的bilibili':
        st.link_button('帮我一键三连', 'https://www.bilibili.com/')

if page == '💭日常分享':
    page_1()
elif page == '🔍实用的小工具':
    page_2()
elif page == '📽️影片推荐':
    page_3()
elif page == '📥留言区':
    page_4()
elif page == '💻其他网站':
    page_5()
