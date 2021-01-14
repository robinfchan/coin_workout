import streamlit as st
import numpy as np
import base64
import pickle
import os

### Start Streamlit###
st.subheader("The World Famous")
st.title("C O I N    W O R K O U T")

go_flip = False
go_flip = st.button('Flip!')
if go_flip == True:
    # get array of nine 0/1
    flips = np.random.randint(2, size = 9)
    workout = []
    #1
    if flips[0] == 0:
        st.write('1: 15 Squats')
        workout.append('1: 15 Squats')
    else:
        st.write('1: 25 Calf Raises')
        workout.append('1: 25 Calf Raises')
    #2
    if flips[0] == 0:
        st.write('2: 60 sec. Jog in Place')
        workout.append('2: 60 sec. Jog in Place')
    else:
        st.write('2: 25 Jumping Jacks')
        workout.append('2: 25 Jumping Jacks')
    #3
    if flips[0] == 0:
        st.write('3: 20 Kneeling Pushups')
        workout.append('3: 20 Kneeling Pushups')
    else:
        st.write('3: 10 Pushups')
        workout.append('3: 10 Pushups')
    #4
    if flips[0] == 0:
        st.write('4: 20 Jumping Jacks')
        workout.append('4: 20 Jumping Jacks')
    else:
        st.write('4: 50 sec. Jog in place')
        workout.append('4: 50 sec. Jog in place')
    #5
    if flips[0] == 0:
        st.write('5: 40 High Knees')
        workout.append('5: 40 High Knees')
    else:
        st.write('5: 40 Jumping Jacks')
        workout.append('5: 40 Jumping Jacks')
    #6
    if flips[0] == 0:
        st.write('6: 35 Crunches')
        workout.append('6: 35 Crunches')
    else:
        st.write('6: 20 Situps')
        workout.append('6: 20 Situps')
    #7
    if flips[0] == 0:
        st.write('7: 10 Push Ups')
        workout.append('7: 10 Push Ups')
    else:
        st.write('7: 20 Kneeling Pushups')
        workout.append('7: 20 Kneeling Pushups')
    #8
    if flips[0] == 0:
        st.write('8: 60s Jog in Place')
        workout.append('8: 60s Jog in Place')
    else:
        st.write('8: 25 Jumping Jacks')
        workout.append('8: 25 Jumping Jacks')
    #9
    if flips[0] == 0:
        st.write('9: 50 Crunches')
        workout.append('9: 50 Crunches')
    else:
        st.write('9: 20 Situps')
        workout.append('9: 20 Situps')

    with open('workout.pickle', 'wb') as fp:
        pickle.dump(workout, fp)

done = st.checkbox('I did it all!')
if done == True:

    if os.path.exists('workout.pickle'):

        pic_num = np.random.randint(4, size = 1)
        pic_sel = f'{int(pic_num)}.GIF'
        file_ = open(pic_sel, "rb")
        contents = file_.read()
        url = base64.b64encode(contents).decode("utf-8")
        file_.close()

        with open('workout.pickle', 'rb') as fp:
            workout = pickle.load(fp)

        st.write("Wow, great work. So proud! Such an athlete!")
        st.text("Your workout:")
        st.text(f'{workout[0]}')
        st.text(f'{workout[1]}')
        st.text(f'{workout[2]}')
        st.text(f'{workout[3]}')
        st.text(f'{workout[4]}')
        st.text(f'{workout[5]}')
        st.text(f'{workout[6]}')
        st.text(f'{workout[7]}')
        st.text(f'{workout[8]}')
        st.markdown(f'<img src="data:image/gif;base64,{url}" alt="done gif">', unsafe_allow_html=True,)

        os.remove('workout.pickle')
    else:
        st.write("CHEATER!")        
