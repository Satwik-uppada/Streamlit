# -----> Required libraries 
import streamlit as st
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu

# -----> Modifying page configurations 
st.set_page_config(layout='wide')

# -----> All functions 

def find_info(obj, function_ask):
    return st.write(getattr(obj,function_ask))
        
def get_help_text(obj, method_name):
    return st.write(getattr(obj, method_name))


# ---------------------------------------------------------------------------- #
home_tab, heading_tab, write_tab, caption_tab, code_tab, divider_tab, echo_tab, latex_tab, text_tab, data_tab, buttons_tab, pop_over_tab = st.tabs([
    '🏠 Home', '🔠 Heading Elements', '📝 Write Elements', '📑 Caption Element', '💻 Code Element', 
    '➖ Divider Element', '🔍 Echo Element', '📚 Latex Element', '✏️ Text Element', '📊 Data Elements', 
    '🅱 Button Element', '📋 Popover Element'
])

with home_tab:
    # -----> page content 
    # Set's the app title
    st.title(":orange[Streamlit Cheat Sheet for Beginners] 📜")
    st.write("꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦")

    # For heading
    st.header(":blue[Streamlit - Cheat Sheet]")

    # For Sub heading
    st.subheader(":green[For Absolute Beginners]")

    # You can display any format of text using write() function
    st.write("In this Cheat sheet, I'll cover every function and some basic web codes.")

    # Markdown gives customization for your text like HTML, JS
    st.markdown(":blue[**Streamlit**:] is a widely used open source Python framework, facilitates the creation and "
                "deployment of web apps for Machine Learning and Data Science.")

    st.markdown(":link: Visit [Streamlit](https://streamlit.io/) to learn more about Streamlit.")

    st.write(":information_source: Before going further, we need to install Streamlit")

    install_code = '''pip install streamlit'''
    st.code(install_code, language='command')

    st.header(":hammer: Let's try to build some basic Web app.")
    st.subheader(":rocket: How to build a basic Web app to print 'Hello world!' on the web...")

    # -----> code element 
    # CODE = it displays the code as you write
    sample_app = '''
    import streamlit as st
    st.write("Hello world!")
    '''
    st.code(sample_app, language='python')

    st.markdown(":desktop_computer: Now open your terminal and run this code using ***streamlit run filename.py***")

    st.write(":tada: Hurray!.. we just created a web application using Streamlit.")

    st.write("---")
    st.subheader("🔍 Explore the Streamlit library............", help="Expand the list!")
    streamlit_fun = dir(st)
    
    st.code('st.help()')

    # -----> function information code
    st.write("---")
    st.subheader(":orange[Need help with any function] 🤔")
    select_option = st.selectbox("Select Option:",streamlit_fun ,index=None)
    
    if select_option:
        st.subheader(f"Information about '{select_option}'")
        find_info(st,select_option)

with heading_tab:
    # -----> Heading elements 
    st.header("🔠 Heading Elements")
    st.write("꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦")
    st.write("Streamlit has three types of headings, let's see...")

    st.header("1. Title")
    st.code('''st.title(body="output: This is title", help="tool tip", anchor=None)
    # body: content of the title
    # help: tool tip next to the title
    # anchor: link for particular portion in the webpage.-->when we touch the heading, it will navigate to the particular line
    ''')
    st.write("output: ")
    st.title(body="This is title", help="tool tip", anchor=None)
    st.divider()

    st.header("2. Header")
    st.code('''st.header("This is first type, called header.", help="header demo", divider="blue", anchor=None)
    # help: display question mark icon to the right. when we click on it, it will display content for more information or specific reason for that heading
    # divider: draw horizontal line after heading with specified color, by default divider = False)
    ''')
    st.write("divider : bool or “blue”, “green”, “orange”, “red”, “violet”, “gray/grey”, or “rainbow”")
    st.write("output: ")
    st.header("This is first type, called header.", help="header demo", divider='blue', anchor=None)
    st.divider()

    st.header("3. Subheader")
    st.code('''st.subheader("This is :blue-background[second type], called :red[sub header].", anchor="https://docs.streamlit.io/get-started", divider="rainbow", help="This is demo of how to use subheader.")
    # :blue-background[content] : display the content with specified background color
    # :red[] : display the text in specified color
    # Note: only below mentioned colors will work
    # colors: [blue, green, orange, red, violet, gray/grey, rainbow]
    # help: display question mark icon to the right. when we click on it, it will display content for more information or specific reason for that heading
    # divider: draw horizontal line after heading with specified color, by default divider = False)
    ''')
    st.write("output: ")
    st.subheader("This is :blue-background[second type], called :red[sub header].", anchor="https://docs.streamlit.io/get-started", divider='rainbow', help="This is demo of how to use subheader.")

    st.write("---")
    st.write("Let's see customized header with markdown")
    st.header("Markdown header")
    st.code('st.markdown("<h1>This is markdown header</h1>", unsafe_allow_html=True)')
    st.markdown("<h1>output: This is markdown header</h1>", unsafe_allow_html=True)
    with st.echo():
        # code taken from Streamlit documentation
        st.markdown("*Streamlit* is **really** ***cool***.")
        st.markdown('''
            :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
            :gray[pretty] :rainbow[colors] and :blue-background[highlight] text.''')
        st.markdown("Here's a bouquet &mdash; :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

with write_tab:
    # -----> Write elements 
    st.header("📝 Write Elements")
    st.write("꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦")

    st.subheader("Write")
    with st.echo():
        st.write("It used to display any type of content like string, dataframes, tables, functions, emojis, graphs, also supports HTML content using unsafe_allow_html.")

    st.subheader("Write_stream")
    with st.echo():
        import time
        import streamlit as st  

        sample_text = "This text will display in the typewriter format. Like chatgpt, the entire text is displayed as specified with a time delay."

        def stream_data():
            for char in sample_text: # we can specify as character or word or customized content like upto , or @ 
                yield char 
                time.sleep(0.02)

        if st.button("Stream the text"):
            st.write_stream(stream_data)

with caption_tab:
    # -----> Streamlit captions
    st.header("📑 Caption Element")
    st.write("꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦")
    with st.echo():
        st.caption("This is the caption which is used to explain the above content, supports *italic*, emojis 😎, :rainbow[colored text], :red-background[background] for text, HTML using unsafe_allow_html parameter.")

with code_tab:
    # -----> Code element
    st.header("💻 Code Element")
    st.write("꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦")
    st.write("Display a code block with optional syntax highlighting.")
    st.code("""
    import streamlit as st

    code = '''def hello():
        print("Hello, Streamlit!")'''
    st.code(code, language='python')
                """, language='python')

with divider_tab:
    # -----> Divider element
    st.header("➖ Divider Element")
    st.write("꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒷꒦꒷꒦꒷꒦")
    st.write("Draw a horizontal line")
    with st.echo():
        st.divider()

    st.write("You can achieve the same with the write element.")
    with st.echo():
        st.write("---")

    st.write("You can also achieve the same with the magic element.")
    with st.echo():
        "---"    
    st.caption("Above horizontal lines are outputs of the codes")

    st.write("---")

with echo_tab:
    # -----> Echo element
    st.header("🔍 Echo Element")
    st.write("꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒷꒦꒷꒦")
    st.write("Use in a with block to draw some code on the app, then execute it.")
    with st.echo():
        with st.echo():# code for echo element, always in the "with block"
            st.write("This content will display on the web app as well as this line of code will also be displayed.")

with latex_tab:
    # -----> Latex element
    st.header("📚 Latex Element")
    st.write("꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒷꒦꒷꒦")
    st.write("Display mathematical expressions formatted as LaTeX.")
    with st.echo():
        st.latex("(a+b)^2 = a^2+b^2+2ab", help="formula")

with text_tab: 
    # -----> Text element
    st.header("✏️ Text Element")
    st.write("꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒷꒦")
    st.write("Write fixed width and preformatted text.")
    import random
    with st.echo():
        text_element = st.text("sample text.")
        list_of_texts = ['hi', "hello", "namasthe"]
        if st.button("Click for text change"):
            random_text = random.choice(list_of_texts)
            text_element.write(random_text)
            # by clicking the button, the text will change respectively.

with data_tab:    
    # -----> Data elements
    st.header("📊 Data Elements")
    st.write("꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒷꒦꒷꒷꒦")
    st.subheader("Dataframe", divider='grey')
    st.write("You can display dataframes as a table on the web interface easily.")
    with st.echo():
        df = pd.DataFrame(np.random.randn(10, 10), columns=("column %d" % i for i in range(10)))
        st.dataframe(df)
    st.info("You can also style the dataframe")
    st.subheader("How to highlight max values in each column", divider='grey')
    
    with st.echo():
        df = pd.DataFrame(np.random.randn(10, 10), columns=("column %d" % i for i in range(10)))
        st.dataframe(df.style.highlight_max(axis=0,color='pink'))
        explanation = """
         df.style.highlight_max() object filter the max value 
         axis = 0 means indicating columns [0: columns, 1: rows]
         df.style.highlight_max(axis=0) : highlight the max values of each column
        """
    # -----> dataframes styles 
    st.subheader("Normal Dataframe", divider='grey')
    with st.echo():
        df = pd.DataFrame({
            "name" : ['Pushpa-The Rule', 'RRR', 'Bahubali-The beginning','Bahubali- The conclusion'],
            "Rating": [7,8,9,9],
            "Views": [[random.randint(1000, 500000) for _ in range(30)] for _ in range(4)]
        })
    with st.echo():
        st.dataframe(df)
    st.subheader("Customized Dataframe using style objects", divider='grey')
    with st.echo():
        st.dataframe(df, column_config={
            "name": "Movie_Name",
            "Rating": st.column_config.NumberColumn(
                "Movie_Rating (out of 10)",
                help="No.of stars for Movie",
                format="%d ⭐"),
            "Views": st.column_config.AreaChartColumn("Views(past 30 days)",y_min=1000,y_max=500000,)

        },hide_index=True)
    

    with st.echo():
        event = st.dataframe(st.session_state.df,on_select="rerun", selection_mode=['multi-column','multi-row'],key='data')   
        event.selection
    # 
    st.header("Want to explore the style objects ❓")
    with st.container(border=True,):
        # Streamlit app layout
        st.subheader(":blue[DataFrame.style Methods Explorer]")
        style_methods = dir(df.style)
# 
        # Dropdown to select a method
        selected_method = st.selectbox("Select a method/attribute:",style_methods,index=None)
        with st.container(border=True):
            # Display detailed help information
            if selected_method:
                st.subheader(f"Information about '{selected_method}'")
               # Capture the help text and display it
                get_help_text(df.style, selected_method)

        
    
    st.markdown(":link: Visit [Streamlit Dataframes](https://docs.streamlit.io/develop/api-reference/data/st.dataframe) to learn more about Streamlit Dataframes.")
    
    st.subheader("Data Editor", divider='grey')
    st.write("You can edit dataframe using this element.")
    with st.echo():
        data = {"name": ['satwik', 'pardhi', 'bujji', 'lokesh'], "bday": [8, 8, 8, 11]}
        st.data_editor(data) 
    
    


# ---------------------------------------------------------------------------- #
with buttons_tab:
    st.header("🅱 Streamlit Buttons")
    
    st.write("꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷")

    st.code("""
    def function_name():
        st.balloons()
        # st.ballons() displays balloons on the web app
    st.button(label="Click me!", help="help with hover effect to display information", on_click=function_name)

    # label: button name.
    # key: unique key for a specific button.
    # type: primary or secondary.
    # help: it gives specialized content on hovering over the button.
    # on_click: it's a callable function.
    # args: gives function arguments in the form of a tuple.
    # kwargs: gives function arguments in the form of a dictionary.
    """)

    st.write("output:")
    def function_name():
        st.balloons()
    st.button(label="Click me!", help="help uses for hover effect to display information", on_click=function_name)

with pop_over_tab:
    st.write("---")
    popover = st.popover("Filter items")
    red = popover.checkbox("Show red items.", True)
    blue = popover.checkbox("Show blue items.", True)

    if red:
        st.write(":red[This is a red item.]")
    if blue:
        st.write(":blue[This is a blue item.]")

    code ="""
    popover = st.popover("Filter items")
    red = popover.checkbox("Show red items.", True)
    blue = popover.checkbox("Show blue items.", True)

    if red:
        st.write(":red[This is a red item.]")
    if blue:
        st.write(":blue[This is a blue item.]")
    """
    st.code(code, language='python')
