import streamlit as st
import streamlit.components.v1 as components
import plotly.graph_objects as go
import base64
from htbuilder import HtmlElement, div, hr, a, p, img, styles
from htbuilder.units import percent, px


def image(src_as_string, **style):
    """ HTML image """
    return img(src=src_as_string, style=styles(**style))


def link(link_, text, **style):
    """ HTML link """
    return a(_href=link_, _target="_blank", style=styles(**style))(text)


def layout(*args):
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

    st.markdown(style, unsafe_allow_html=True)

    for arg in args:
        if isinstance(arg, str):
            body(arg)

        elif isinstance(arg, HtmlElement):
            body(arg)

    st.markdown(str(foot), unsafe_allow_html=True)


footer_args = [
    link('mailto:emmanuel.pean@gmail.com',
         image('https://raw.githubusercontent.com/Emmanuelpean/PersonnalWebsite/main/images/email.png', height=px(30))),
    "&nbsp &nbsp ",
    link('https://www.researchgate.net/profile/Emmanuel-Pean-2',
         image('https://raw.githubusercontent.com/Emmanuelpean/PersonnalWebsite/main/images/researchgate.png',
               height=px(30))),
    "&nbsp &nbsp ",
    link('https://twitter.com/emmanuel_pean',
         image('https://raw.githubusercontent.com/Emmanuelpean/PersonnalWebsite/main/images/twitter.png',
               height=px(30))),
    "&nbsp &nbsp ",
    link('https://orcid.org/0000-0002-3056-5286',
         image('https://raw.githubusercontent.com/Emmanuelpean/PersonnalWebsite/main/images/orcid.png', height=px(30))),
    "&nbsp &nbsp ",
    link('https://www.linkedin.com/in/emmanuelpean',
         image('https://raw.githubusercontent.com/Emmanuelpean/PersonnalWebsite/main/images/linkedin.png',
               height=px(30))),
    "&nbsp &nbsp ",
    link('https://www.scopus.com/authid/detail.uri?authorId=57190185586',
         image('https://raw.githubusercontent.com/Emmanuelpean/PersonnalWebsite/main/images/scopus.png',
               height=px(30)))]


@st.cache
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
layout(*footer_args)
st.markdown("""%s""" % render_image("images/photo.png", 15, 'png'), unsafe_allow_html=True)  # main logo
st.markdown("<h1 style='text-align: center;'>Dr Emmanuel V. Péan</h1>", unsafe_allow_html=True)
st.markdown("""#""")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("""
    #### About me
    I am an early career researcher who has recently completed a PhD on the photochemistry of perovskite materials for use 
    in photovoltaics. I am deeply concerned about the state of the environment and climate change. I am hardworking, 
    diligent and always ready to go beyond my assignment to produce high quality work. My programming skills allow me to 
    quickly process and analyse large amounts of data. I am also resourceful and able to write software complemented with 
    3D printer apparatus for e.g. automating experiments.""", icon='👨')

    st.markdown("""
    #### Skills
    Hover on a category for more information""")
    fig = go.Figure(data=go.Barpolar(
        r=[4.5, 4, 2, 4, 2.5, 4, 4],
        theta=['Python Programming', 'Data Processing', 'Matlab Programming', 'Data Presentations', '3D Modelling',
               '3D Printing', 'Experiment automation'],
        text=[
            'I mainly use Python for data processing and analysing data,<br>as well as simulations (*e.g.* charge carrier recombination),<br>to automate experiments, and website making.',
            'Thanks to my programming knowledge, I am able to quickly<br>perform complex data processing on large amount of data',
            'I used to a Matlab student demonstrator and thus know the basics of the language',
            'I take pride in presenting my research in the most accessible way,<br>making sure that my figures are as clear and understandable as possible',
            'I use Solidworks to design models for 3D printing',
            'I use 3D printing in order to  build experimental setups and automate experiments',
            'Thanks to my programming and 3D printing skills, I am able to automatise my experiments,<br>which improves their reliability and saves me time'],
        hoverinfo='text',
        width=[0.7] * 7,
        marker_color=["#E4FF87", '#709BFF', '#FFAA70', '#FFDF70', '#709BFF', '#B6FFB4', '#FFAA70'],
        marker_line_color="black",
        marker_line_width=1.5,
        opacity=0.8))
    fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 5], ticklabelstep=1)))

    st.plotly_chart(fig)

    st.success("""
    #### Awards
    * 2021 Swansea University Material Research Centre Rose Bowl prize for best thesis
    * Best Poster prize at the 2020 SUNRISE online meeting and best ECR presentation runner-up prize at the 2022 SUNRISE online meeting
    * 2019 Swansea University, School of Engineering 3 minutes thesis winner
    * Research as Art: 2017 Imagination and 2018 runner-up prizes
    * 2016 Best Master’s internship in material science in the west of France awarded by the Société Française de Métallurgie et Matériaux""",
               icon="🏆")

    st.warning("""
    #### Scholarship, Grants, Fellowships and Memberships
    * 2022 IMPACT fellowship (£35,000)
    * RSC Travel Grant (2017)
    * Supergen Super Solar International and Industrial engagement grant (£1,430) to travel to Delft (NL) as part of a collaboration (2022)
    * Zienkiewicz PhD Scholarship
    * Member of the Royal Society of Chemistry""", icon="🏛")

with col2:
    st.success("""
    #### Research Experience
    **Investigating charge carrier dynamics in organic and inorganic materials using time-resolved microwave conductivity (Research Fellow, March 2022, IMPACT, Swansea University, UK)**
    I am currently working on building a time-resolved microwave photoconductivity setup to investigate charge carrier dynamics in perovskite solar cells.

    **Investigating charge carrier recombination and time-resolved photoluminescence of perovskite materials for solar cell applications (Postdoc, July 2020, SPECIFIC, Swansea University, UK)**
    My role was to investigate charge carrier recombination in perovskite materials using simulations and experimental measurement of time-resolved photoluminescence and how these can be used to improve the efficient of perovskite solar cells.

    **Unraveling the photochemistry of perovskite materials for solar cell applications (PhD, October 2016 - March 2020, Swansea University, Swansea, UK)**
    My PhD project focused on the photochemical properties of perovskite materials for photovoltaic applications. I studied 
    photobrightening, photodarkening, charge carrier recombination kinetic and superoxide formation in perovskites using a wide range of 
    experimental techniques including time-resolved and steady-state fluorescence spectroscopy, x-ray diffractometry, optical and electron microscopy, 
    spectrophotometry and the dihydroethidium fluorescence probe.

    **Investigating point defects in CdIn2S4 through density function theory (MSc thesis, February-June 2016, Institut des matériaux de Nantes - CNRS, Nantes, France)**
    Using density functional theory, I calculated the formation energy of point defects in the CdIn2S4 and related it to the experimentally 
    measured doping. I also developed a software to plot density of states and calculate the formation energy and concentration of point defects 
    in semiconductors from output files from the Vienna Ab Initio Simulation Package software.

    **Electric grid modelling and simulation (April-May 2015, Centre for Integrated Renewable Energy Generation and Supply, Cardiff, UK)**
    I studied the role of electric interconnections between France and Great Britain in the integration of renewable energy sources in 2030 using the PLEXOS Integrated Energy Model software.""",
               icon="🔬")

    st.warning("""
    #### Main publications
    
    * “[Interpreting time-resolved photoluminescence of perovskite materials](https://doi.org/10.1039/D0CP04950F)”, Physical Chemistry Chemical Physics, 2020

    * “[Investigating the Superoxide Formation and Stability in Mesoporous Carbon Perovskite Solar Cells with an Aminovaleric Acid Additive](https://doi.org/10.1002/adfm.201909839)”, Advanced Functional Materials, 2020

    * “[Shining a light on the photoluminescence behaviour of methylammonium lead iodide perovskite: investigating the competing photobrightening and photodarkening processes](https://doi.org/10.1016/j.matlet.2019.01.103)”, Material Letters, 2019 

    * “[Theoretical investigation of CdIn2S4: A possible substitute for CdS in CuIn1-xGaxSe2-based photovoltaic devices](https://doi.org/10.1103/PhysRevMaterials.1.064605)”, Physical Review Materials, 2017

    * “[Presentation of the PyDEF post- treatment Python software to compute publishable charts for Defect Energy Formation](https://doi.org/10.1016/j.cplett.2017.01.001)”, Chemical Physics Letters, 2017

    * “[Role of the GB-France electricity interconnectors in integration of variable renewable generation](https://doi.org/10.1016/j.renene.2016.06.057)”, Renewable Energy, 2016""",
               icon="📚")

    st.success("""
    #### Teaching experience
    * 1st year and 2nd year Matlab demonstrator at Swansea University.
    * Lecture on UV-Vis spectroscopy to 1st year engineering doctorate students part of the Application of Instrumental and Analytical techniques course at Swansea University.
    * Supervision of MSc project: Investigating Diffusion and Charge Carrier Extraction on Charge Carrier Dynamics in Perovskite Thin Films""",
               icon="👨‍🏫")

with col3:
    st.warning("""
    #### My websites
    **[PEARS](https://pears-tool.herokuapp.com)** is a tool to easily fit time-resolved photoluminescence (TRPL) data of perovskite materials. Functionalities include:
    * 2 charge carrier recombination models can be used
    * Basic data processing
    * Customisable fitting parameters
    * Charge carrier recombination process contribution calculation
    * Charge carrier accumulation calculation
    * Advanced analysis using grid fitting

    **[RAFT](https://raft-tool.streamlitapp.com)** is a simple tool able to read and plot a wide range of data files. Functionalities include: 
    * Read 21 different file formats
    * Display single column or multiple column files
    * Basic data processing including, smoothing, max/min point and FWHM calculation""", icon="💻")

    st.info("""
    #### Presentations
    
    * "Interpreting time-resolved photoluminescence of perovskite materials", *9th Bi-annual SUNRISE Symposium*, Online, 2022 (runner-up prize)
    
    * “Stability and Sustainability: Developments in Perovskite Photovoltaics”, *XXIX International Materials Research Congress*, online, 2021.
    
    * “Interpreting Time-Resolved Photoluminescence of Perovskite Materials”, *nanoGe Fall Meeting*, online, 2020.

    * “Modelling charge recombination kinetics in perovskite materials”, *Super solar meeting*, Swansea, UK, 2019.

    * “Photoluminescence kinetic analysis of perovskite materials”, *Workshop on Photoluminescence analysis of photoactive materials*, Swansea, UK, 2019.

    * “Understanding the oxygen and light stability of mesoporous carbon based perovskite solar cells“, *RSC Photochemistry Group Early Career Members Meeting*, Swansea, UK, 2018.

    * “Investigating the effect of the atmosphere on the photoluminescence of methylammonium lead iodide perovskite”, *Photovoltaics and Thermal Analysis Linkam Workshop*, Swansea, UK, 2018.

    * “Explanation and rationalisation of the optoelectronic properties using DFT: stability, doping and modulation”, *Annual day of the West section of the SF2M*, Nantes, France, 2017.""",
            icon="📈")

    st.warning("""
    #### Posters
    
    * “[Investigating the superoxide formation and stability in mesoporous carbon perovskite solar cells with an aminovaleric acid additive](https://raw.githubusercontent.com/Emmanuelpean/PersonnalWebsite/main/posters/Sunrise_2020.pdf)”, *SUNRISE online conference*, 2020 (prize for “Best poster”)
    
    * “[Investigating charge carrier recombination in perovskite materials](https://raw.githubusercontent.com/Emmanuelpean/PersonnalWebsite/main/posters/RSC150120.pdf)”, *RSC Next Generation Materials for Solar Photovoltaics*, London, UK, 2020
    
    * “[Shining a light on the photoluminescence behaviour of methylammonium lead iodide perovskite: investigating the competing photobrightening and photodarkening processes](https://raw.githubusercontent.com/Emmanuelpean/PersonnalWebsite/main/posters/SerSol200319.pdf)”, *Sêr Solar - end of project celebration*, 2019.""",
               icon="📊")

components.html("""<script async defer data-website-id="820a9cf5-cbf2-430f-aff1-c6b647194d74" 
src="https://pears-tracking.herokuapp.com/umami.js"></script>""")
