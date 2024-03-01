'''我的主页'''
import streamlit as st

page = st.sidebar.radio('我的首页',['我的兴趣推荐', '我的图片处理工具', '我的智慧词典', '我的留言区'])

def page_1():
    '''我的兴趣推荐'''
    with open('编程猫的梦想.mp3', 'rb') as f:
        mymp3 = f.read()
    st.audio(mymp3, format='audio/mp3', start_time=0)
    st.image('bcm.png')
    st.write('电影推荐')
    st.write('-----------------------------')
    st.write('游戏推荐')
    st.write('-----------------------------')
    st.write('书籍推荐')
    st.write('-----------------------------')
    st.write('习题集推荐')
    st.write('-----------------------------')

def page_2():
    '''我的图片处理工具'''
    pass

def page_3():
    '''我的智慧词典'''
    pass

def page_4():
    '''我的留言区'''
    pass

if page == '我的兴趣推荐':
    pass
elif page == '我的图片处理工具':
    page_2()
elif page == '我的智慧词典':
    page_3()
elif page == '我的留言区':
    page_4()


