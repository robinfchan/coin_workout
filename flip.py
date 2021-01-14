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
        st.write('Heads: 15 Jump Squats')
        workout.append('Heads: 15 Jump Squats')
    else:
        st.write('Tails: 25 Calf Raises')
        workout.append('Tails: 25 Calf Raises')
    #2
    if flips[1] == 0:
        st.write('Heads: 60 sec. Jog in Place')
        workout.append('Heads: 60 sec. Jog in Place')
    else:
        st.write('Tails: 25 Jumping Jacks')
        workout.append('Tails: 25 Jumping Jacks')
    #3
    if flips[2] == 0:
        st.write('Heads: 20 Kneeling Pushups')
        workout.append('Heads: 20 Kneeling Pushups')
    else:
        st.write('Tails: 10 Pushups')
        workout.append('Tails: 10 Pushups')
    #4
    if flips[3] == 0:
        st.write('Heads: 20 Jumping Jacks')
        workout.append('Heads: 20 Jumping Jacks')
    else:
        st.write('Tails: 50 sec. Jog in Place')
        workout.append('Tails: 50 sec. Jog in Place')
    #5
    if flips[4] == 0:
        st.write('Heads: 40 High Knees')
        workout.append('Heads: 40 High Knees')
    else:
        st.write('Tails: 40 Jumping Jacks')
        workout.append('Tails: 40 Jumping Jacks')
    #6
    if flips[5] == 0:
        st.write('Heads: 35 Crunches')
        workout.append('Heads: 35 Crunches')
    else:
        st.write('Tails: 20 Situps')
        workout.append('Tails: 20 Situps')
    #7
    if flips[6] == 0:
        st.write('Heads: 10 Push Ups')
        workout.append('Heads: 10 Push Ups')
    else:
        st.write('Tails: 20 Kneeling Pushups')
        workout.append('Tails: 20 Kneeling Pushups')
    #8
    if flips[7] == 0:
        st.write('Heads: 60s Jog in Place')
        workout.append('Heads: 60s Jog in Place')
    else:
        st.write('Tails: 25 Jumping Jacks')
        workout.append('Tails: 25 Jumping Jacks')
    #9
    if flips[8] == 0:
        st.write('Heads: 50 Crunches')
        workout.append('Heads: 50 Crunches')
    else:
        st.write('Tails: 20 Situps')
        workout.append('Tails: 20 Situps')

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
        if os.path.exists('workout.pickle'):
            os.remove('workout.pickle')
