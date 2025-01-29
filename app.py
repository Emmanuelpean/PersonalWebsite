import base64
import os

import streamlit as st
from PIL import Image
from htbuilder import HtmlElement, div, hr, a, p, img, styles
from htbuilder.units import percent, px
# noinspection PyPackageRequirements,PyUnresolvedReferences
from markdown import markdown
from streamlit_carousel import carousel

colors = ['#73bff9', '#479ff8', '#3274b5', '#1e4c7c', '#173d5d'] * 2


# ------------------------------------------------------- FOOTER -------------------------------------------------------


def image(src_as_string, **style):
    """ HTML image """
    return img(src=src_as_string, style=styles(**style))


def link(link_, text, **style):
    """ HTML link """
    return a(_href=link_, _target="_blank", style=styles(**style))(text)


def footed_layout(*args):
    style = """
    <style>
      #MainMenu {visibility: hidden;}
      footer {visibility: hidden;}
     .stApp { bottom: 60px; }
    </style>
    """

    style_div = styles(position="fixed", left=0, bottom=0, margin=px(0, 0, 0, 0), width=percent(100), color="black",
                       text_align="center", height="auto", opacity=1)

    style_hr = styles(display="block", margin=px(8, 8, "auto", "auto"), border_style="inset", border_width=px(0))

    body = p()
    foot = div(style=style_div)(hr(style=style_hr), body)

    # noinspection PyTestUnpassedFixture
    st.markdown(style, unsafe_allow_html=True)

    for arg in args:
        if isinstance(arg, str):
            body(arg)

        elif isinstance(arg, HtmlElement):
            body(arg)

    # noinspection PyTestUnpassedFixture
    st.markdown(str(foot), unsafe_allow_html=True)


footer_args = [
    link('mailto:emmanuel.pean@gmail.com',
         image('https://raw.githubusercontent.com/Emmanuelpean/PersonalWebsite/main/images/email.png', height=px(30))),
    "&nbsp &nbsp ",
    link('https://www.researchgate.net/profile/Emmanuel-Pean-2',
         image('https://raw.githubusercontent.com/Emmanuelpean/PersonalWebsite/main/images/researchgate.png',
               height=px(30))),
    "&nbsp &nbsp ",
    link('https://orcid.org/0000-0002-3056-5286',
         image('https://raw.githubusercontent.com/Emmanuelpean/PersonalWebsite/main/images/orcid.png', height=px(30))),
    "&nbsp &nbsp ",
    link('https://www.linkedin.com/in/emmanuelpean',
         image('https://raw.githubusercontent.com/Emmanuelpean/PersonalWebsite/main/images/linkedin.png',
               height=px(30))),
    "&nbsp &nbsp ",
    link('https://www.scopus.com/authid/detail.uri?authorId=57190185586',
         image('https://raw.githubusercontent.com/Emmanuelpean/PersonalWebsite/main/images/scopus.png',
               height=px(30)))]


# -------------------------------------------------------- MAIN --------------------------------------------------------


def custom_text_widget(message, color, alpha=1.0, text_color="white"):
    # Ensure alpha is between 0 and 1
    alpha = max(0, min(alpha, 1))

    # Convert hex color to RGBA
    if color.startswith("#") and len(color) == 7:
        r = int(color[1:3], 16)
        g = int(color[3:5], 16)
        b = int(color[5:7], 16)
        rgba_color = f"rgba({r}, {g}, {b}, {alpha})"
    else:
        rgba_color = color  # Fallback for directly passing an RGBA or named color

    # Convert Markdown to HTML
    message_html = markdown(message)

    # Use st.markdown to create a custom styled box
    # noinspection PyTestUnpassedFixture
    st.markdown(
        f"""
        <div style="
            background-color: {rgba_color};
            color: {text_color};
            padding: 10px;
            border-radius: 5px;
            font-size: 16px;
            margin-bottom: 10px;
            display: flex;
            align-items: flex-start;
        ">
            <div style="flex: 1; font-size: inherit;">
                {message_html}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


@st.cache_resource
def render_image(svg_file, width=100, itype='svg'):
    """ Render a svg file
    :param str svg_file: file path
    :param int width: width in percent
    :param str itype: image type"""

    with open(svg_file, "rb") as ofile:
        svg = base64.b64encode(ofile.read()).decode()
        return '<center><img src="data:image/%s+xml;base64,%s" id="responsive-image" width="%s%%"/></center>' % (
            itype, svg, width)


st.set_page_config('Dr Emmanuel V. Péan', layout='wide')
footed_layout(*footer_args)
st.markdown("""%s""" % render_image("images/photo.png", 15, 'png'), unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'>Dr Emmanuel V. Péan</h1>", unsafe_allow_html=True)
st.markdown('<h2 style="text-align: center; color: rgb(30, 76, 124);">R&D Engineer | System Integration | Automation | Data Analysis</h2>', unsafe_allow_html=True)
st.markdown("""#\n""")

# Load the images
if 'images' not in st.session_state:
    images = ['RaA/' + f for f in os.listdir('RaA') if f.endswith('.jpeg')]
    st.session_state.images = [Image.open(image) for image in images]

col1, col2 = st.columns(2)

with col1:
    custom_text_widget("###👨 About me"
                       "\nI hold a PhD in Materials Science and Engineering with a focus on photochemistry "
                       "and spectroscopy. Proactive and driven by challenges, I thrive on solving complex scientific "
                       "problems by designing innovative, high-quality solutions. I specialise in automation, data "
                       "analysis, and system development, leveraging my expertise to optimise research processes, "
                       "improve efficiency, and ensure precise and accurate results. Passionate about advancing "
                       "technology, I am dedicated to creating cutting-edge tools and systems that meet the complex "
                       "and evolving needs of scientific research.", color=colors[0])

    st.markdown("#### 🏛 Education & Academic Carrier")
    st.image('images/Education.png')

    custom_text_widget("#### 🔬 Key Achievements"
                       "\n##### Full automated photoluminescence quantum efficiency setup"
                       "\nSpearheaded the design and implementation of a fully automated photoluminescence quantum efficiency "
                       "setup. Ensured the project was kept to budget constraints, integrating Python-based user-friendly software "
                       "and robotic sample handling. This innovation reduced operator workload by enabling up to 24 samples to be "
                       "measured with a single 30-minute setup, eliminating the need for manual sample loading every 25 minutes. "
                       "Additionally, it introduced advanced measurement capabilities, enabling deeper insights into the absorber "
                       "layer quality previously unattainable with the non-automated setup."

                       "\n##### Fully interactive and customisable dashboard"
                       "\nProposed and developed an interactive, user-customisable dashboard featuring advanced analysis "
                       "tools for visualising and analysing data. Designed and implemented the accompanying custom Python "
                       "API to enable seamless database integration. This tool allowed engineers to monitor data trends "
                       "over time and accelerated the process of plotting experimental results by approximately tenfold "
                       "compared to using database queries and JMP plotting."

                       "\n#####Investigating charge carrier dynamics in organic and inorganic materials using time-resolved microwave conductivity"
                       "\nSecured a competitive £85,000 grant to design and build a time-resolved microwave photoconductivity "
                       "setup. This advanced setup, comprising 28 distinct components, featured computer-controlled automation "
                       "of nine key elements through a robust Python-based GUI, enabling the streamlined execution of complex "
                       "measurements to advance perovskite material research. Numerous parts of the setup were designed using "
                       "SolidWorks and then 3D printed, allowing for a fully customised and compact design.",
                       color=colors[1])

    st.markdown("#### 💽 Software")
    software_items = [dict(img='softwares/' + f, title='', text='') for f in os.listdir('softwares') if
                      f.endswith('_.png')]
    carousel(items=software_items, container_height=600, width=1)

    custom_text_widget("####🏆 Awards"
                       "\n* 2021 Swansea University Material Research Centre Rose Bowl prize for best thesis"
                       "\n* Best Poster prize at the 2020 SUNRISE online meeting and best ECR presentation runner-up prize at the 2022 SUNRISE online meeting"
                       "\n* 2019 Swansea University, School of Engineering 3 minutes thesis winner* Research as Art: 2017 Imagination and 2018 runner-up prizes"
                       "\n* 2016 Best Master’s internship in material science in the west of France awarded by the Société Française de Métallurgie et Matériaux",
                       color=colors[2])

    custom_text_widget("####💻 My Websites"
                       "\n**[PEARS](https://pears-tool.herokuapp.com)** is a tool to easily fit time-resolved photoluminescence (TRPL) data of perovskite materials. Functionalities include:\n"
                       "\n* 2 charge carrier recombination models can be used"
                       "\n* Basic data processing"
                       "\n* Customisable fitting parameters"
                       "\n* Charge carrier recombination process contribution calculation"
                       "\n* Charge carrier accumulation calculation"
                       "\n* Advanced analysis using grid fitting\n"
                       "\n**[RAFT](https://raft-tool.streamlitapp.com)** is a simple tool able to read and plot a wide range of data files. Functionalities include: \n"
                       "\n* Reading 21 different file formats"
                       "\n* Displaying single column or multiple column files"
                       "\n* Basic data processing, including smoothing, max/min point and FWHM calculation)",
                       color=colors[3])

with col2:
    custom_text_widget("#### Scholarship, Grants, Fellowships and Memberships"
                       "\n* 2022 IMPACT fellowship (£85,000)"
                       "\n* RSC Travel Grant (2017)"
                       "\n* Supergen Super Solar International and Industrial engagement grant (£1,430) to travel to Delft (NL) as part of a collaboration (2022)"
                       "\n* Zienkiewicz PhD Scholarship"
                       "\n* Member of the Royal Society of Chemistry",
                       color=colors[4])

    custom_text_widget("####📚 Publications\n"
                       "\n* “[Interpreting time-resolved photoluminescence of perovskite materials](https://doi.org/10.1039/D0CP04950F)”, Physical Chemistry Chemical Physics, 2020"
                       "\n* “[Investigating the Superoxide Formation and Stability in Mesoporous Carbon Perovskite Solar Cells with an Aminovaleric Acid Additive](https://doi.org/10.1002/adfm.201909839)”, Advanced Functional Materials, 2020"
                       "\n* “[Shining a light on the photoluminescence behaviour of methylammonium lead iodide perovskite: investigating the competing photobrightening and photodarkening processes](https://doi.org/10.1016/j.matlet.2019.01.103)”, Material Letters, 2019 "
                       "\n* “[Theoretical investigation of CdIn2S4: A possible substitute for CdS in CuIn1-xGaxSe2-based photovoltaic devices](https://doi.org/10.1103/PhysRevMaterials.1.064605)”, Physical Review Materials, 2017"
                       "\n* “[Presentation of the PyDEF post- treatment Python software to compute publishable charts for Defect Energy Formation](https://doi.org/10.1016/j.cplett.2017.01.001)”, Chemical Physics Letters, 2017"
                       "\n* “[Role of the GB-France electricity interconnectors in integration of variable renewable generation](https://doi.org/10.1016/j.renene.2016.06.057)”, Renewable Energy, 2016",
                       color=colors[5])

    custom_text_widget("####👨‍🏫 Teaching Experience"
                       "\n* 1st year and 2nd year Matlab demonstrator at Swansea University."
                       "\n* Lecture on UV-Vis spectroscopy to 1st year engineering doctorate students part of the Application of Instrumental and Analytical techniques course at Swansea University."
                       "\n* Supervision of MSc project: Investigating Diffusion and Charge Carrier Extraction on Charge Carrier Dynamics in Perovskite Thin Films",
                       color=colors[6])

    custom_text_widget("#### 👨‍🏫 Presentations"
                       "\n* “Interpreting time-resolved photoluminescence of perovskite materials”, *9th Bi-annual SUNRISE Symposium*, Online, 2022 (runner-up prize)"
                       "\n* “Stability and Sustainability: Developments in Perovskite Photovoltaics”, *XXIX International Materials Research Congress*, online, 2021."
                       "\n* “Interpreting Time-Resolved Photoluminescence of Perovskite Materials”, *nanoGe Fall Meeting*, online, 2020."
                       "\n* “Modelling charge recombination kinetics in perovskite materials”, *Super solar meeting*, Swansea, UK, 2019."
                       "\n* “Photoluminescence kinetic analysis of perovskite materials”, *Workshop on Photoluminescence analysis of photoactive materials*, Swansea, UK, 2019."
                       "\n* “Understanding the oxygen and light stability of mesoporous carbon based perovskite solar cells“, *RSC Photochemistry Group Early Career Members Meeting*, Swansea, UK, 2018."
                       "\n* “Investigating the effect of the atmosphere on the photoluminescence of methylammonium lead iodide perovskite”, *Photovoltaics and Thermal Analysis Linkam Workshop*, Swansea, UK, 2018."
                       "\n* “Explanation and rationalisation of the optoelectronic properties using DFT: stability, doping and modulation”, *Annual day of the West section of the SF2M*, Nantes, France, 2017.",
                       color=colors[7])

    custom_text_widget("####📊 Posters"
                       "\n* “[Investigating the superoxide formation and stability in mesoporous carbon perovskite solar cells with an aminovaleric acid additive](https://raw.githubusercontent.com/Emmanuelpean/PersonalWebsite/main/posters/Sunrise_2020.pdf)”, *SUNRISE online conference*, 2020 (prize for “Best poster”)"
                       "\n* “[Investigating charge carrier recombination in perovskite materials](https://raw.githubusercontent.com/Emmanuelpean/PersonalWebsite/main/posters/RSC150120.pdf)”, *RSC Next Generation Materials for Solar Photovoltaics*, London, UK, 2020"
                       "\n* “[Shining a light on the photoluminescence behaviour of methylammonium lead iodide perovskite: investigating the competing photobrightening and photodarkening processes](https://raw.githubusercontent.com/Emmanuelpean/PersonalWebsite/main/posters/SerSol200319.pdf)”, *Sêr Solar - end of project celebration*, 2019.""",
                       color=colors[8])

    RaA_items = [dict(img='RaA/' + f, title='', text='') for f in os.listdir('RaA') if f.endswith('.jpeg')]

    carousel(items=RaA_items, container_height=1000)
