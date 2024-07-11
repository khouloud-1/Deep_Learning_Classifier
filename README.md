<html xmlns:v="urn:schemas-microsoft-com:vml"
xmlns:o="urn:schemas-microsoft-com:office:office"
xmlns:w="urn:schemas-microsoft-com:office:word"
xmlns:dt="uuid:C2F41010-65B3-11d1-A29F-00AA00C14882"
xmlns:m="http://schemas.microsoft.com/office/2004/12/omml"
xmlns="http://www.w3.org/TR/REC-html40">

<head>
<meta http-equiv=Content-Type content="text/html; charset=windows-1252">
<meta name=ProgId content=Word.Document>
<meta name=Generator content="Microsoft Word 15">
<meta name=Originator content="Microsoft Word 15">
<link rel=File-List href="index_files/filelist.xml">
<link rel=Edit-Time-Data href="index_files/editdata.mso">
<link rel=dataStoreItem href="index_files/item0001.xml"
target="index_files/props002.xml">
<link rel=themeData href="index_files/themedata.thmx">
<link rel=colorSchemeMapping href="index_files/colorschememapping.xml">
</head>

<body lang=EN-US link=blue vlink=purple style='tab-interval:35.4pt;word-wrap:
break-word'>

<div class=WordSection1>

<p class=MsoNormal align=center style='margin-bottom:0in;text-align:center;
line-height:150%'><b><span style='font-size:40.0pt;line-height:150%;mso-ansi-language:
EN-US'>Deep Learning for Hierarchical Arabic Text Classification<o:p></o:p></span></b></p>

<p class=MsoNormal style='margin-bottom:0in;text-align:justify;line-height:
150%'><span style='mso-ansi-language:EN-US'><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal style='margin-bottom:0in;text-align:justify'><span
style='mso-ansi-language:EN-US'><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal align=center style='margin-bottom:0in;text-align:center;
line-height:150%'><b><span style='font-size:10.0pt;line-height:150%;mso-bidi-font-family:
Calibri;mso-bidi-theme-font:minor-latin;color:black;mso-ansi-language:EN-US'>Djelloul
BOUCHIHA<sup>1</sup>, Abdelghani BOUZIANE<sup>2</sup>, Noureddine DOUMI<sup>3</sup>,
Farouk Omar BERBOUCHI<sup>4</sup>, Aymen Abdelghani KIBIR<sup>5</sup>, Nihad
MEBARKI<sup>6</sup> and Badia Achouak BENAMER<sup>7</sup><o:p></o:p></span></b></p>

<p class=MsoNormal style='text-align:justify;line-height:normal'><b><span
style='mso-ansi-language:EN-US'><o:p>&nbsp;</o:p></span></b></p>

<p class=MsoNormal style='text-align:justify;line-height:normal'><b><span
style='font-size:14.0pt;mso-ansi-language:EN-US'>If you use a software from
this page, please cite us as follows:<o:p></o:p></span></b></p>

<p class=MsoNormal style='text-align:justify;line-height:normal'><b><span
style='font-size:10.0pt;mso-bidi-font-family:Calibri;mso-bidi-theme-font:minor-latin;
color:black;mso-ansi-language:EN-US'>Djelloul BOUCHIHA, Abdelghani BOUZIANE,
Noureddine DOUMI, Farouk Omar BERBOUCHI, Aymen Abdelghani KIBIR, Nihad MEBARKI
and Badia Achouak BENAMER</span></b><span style='font-size:14.0pt;mso-ansi-language:
EN-US'>. <b>Deep Learning for Hierarchical Arabic Text Classification</b>.
Submitted (still under review).<o:p></o:p></span></p>

<p class=MsoNormal style='text-align:justify;line-height:normal'><span
style='font-size:14.0pt;mso-ansi-language:EN-US'><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal style='text-align:justify;line-height:normal'><b><span
style='font-size:14.0pt;mso-ansi-language:EN-US'>If you need help, contact </span></b><span
style='font-size:14.0pt;mso-ansi-language:EN-US'>Djelloul BOUCHIHA<b>: <o:p></o:p></b></span></p>

<p class=MsoNormal style='text-align:justify;line-height:normal'><span lang=FR><a
href="mailto:bouchiha@cuniv-naama.dz"><span lang=EN-US style='font-size:14.0pt;
mso-ansi-language:EN-US'>bouchiha@cuniv-naama.dz</span></a></span><span
style='font-size:14.0pt;mso-ansi-language:EN-US'>; </span><span lang=FR><a
href="mailto:bouchiha.dj@gmail.com"><span lang=EN-US style='font-size:14.0pt;
mso-ansi-language:EN-US'>bouchiha.dj@gmail.com</span></a></span><span
style='font-size:14.0pt;mso-ansi-language:EN-US'>; </span><span lang=FR><a
href="mailto:djelloul.bouchiha@univ-sba.dz"><span lang=EN-US style='font-size:
14.0pt;mso-ansi-language:EN-US'>djelloul.bouchiha@univ-sba.dz</span></a></span><span
style='font-size:14.0pt;mso-ansi-language:EN-US'>; <o:p></o:p></span></p>

<p class=MsoNormal style='text-align:justify;line-height:normal'><span
style='font-size:14.0pt;mso-ansi-language:EN-US'><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal style='text-align:justify;line-height:normal'><b><span
style='font-size:14.0pt;mso-ansi-language:EN-US'>Before using any software from
this page, please follow carefully the following notes:<o:p></o:p></span></b></p>

<p class=MsoNormal style='text-align:justify;line-height:normal'><span
style='mso-ansi-language:EN-US'><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal style='text-align:justify;line-height:normal'><span
style='font-size:14.0pt;mso-ansi-language:EN-US'>First you have to download the
WiHArD dataset from </span><span lang=FR style='font-size:14.0pt'><a
href="https://data.mendeley.com/datasets/kdkryh5rs2/2"><span lang=EN-US
style='mso-ansi-language:EN-US'>https://data.mendeley.com/datasets/kdkryh5rs2/2</span></a></span><span
style='font-size:14.0pt;mso-ansi-language:EN-US'>. Download the whole dataset as
one CSV file (</span><span style='font-size:14.0pt;font-family:"Arial",sans-serif;
color:#1A1A1A;mso-ansi-language:EN-US'><a
href="https://data.mendeley.com/datasets/kdkryh5rs2/2#:~:text=CSV-,WiHArD.csv,-3%20MB">WiHArD.csv</a></span><span
style='font-size:14.0pt;mso-ansi-language:EN-US'>)<o:p></o:p></span></p>

<p class=MsoNormal style='text-align:justify;line-height:normal'><span
style='font-size:14.0pt;mso-ansi-language:EN-US'><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal style='text-align:justify;line-height:normal'><b><span
style='font-size:14.0pt;mso-ansi-language:EN-US'>Note that the deep learning classifier
has been implemented using the Scientific Python Development Environment
(Spyder IDE, version 4.1.5):<o:p></o:p></span></b></p>

<p class=MsoNormal style='text-align:justify;line-height:normal'><span lang=FR
style='font-size:14.0pt;mso-fareast-language:FR;mso-no-proof:yes'><v:shapetype
 id="_x0000_t75" coordsize="21600,21600" o:spt="75" o:preferrelative="t"
 path="m@4@5l@4@11@9@11@9@5xe" filled="f" stroked="f">
 <v:stroke joinstyle="miter"/>
 <v:formulas>
  <v:f eqn="if lineDrawn pixelLineWidth 0"/>
  <v:f eqn="sum @0 1 0"/>
  <v:f eqn="sum 0 0 @1"/>
  <v:f eqn="prod @2 1 2"/>
  <v:f eqn="prod @3 21600 pixelWidth"/>
  <v:f eqn="prod @3 21600 pixelHeight"/>
  <v:f eqn="sum @0 0 1"/>
  <v:f eqn="prod @6 1 2"/>
  <v:f eqn="prod @7 21600 pixelWidth"/>
  <v:f eqn="sum @8 21600 0"/>
  <v:f eqn="prod @7 21600 pixelHeight"/>
  <v:f eqn="sum @10 21600 0"/>
 </v:formulas>
 <v:path o:extrusionok="f" gradientshapeok="t" o:connecttype="rect"/>
 <o:lock v:ext="edit" aspectratio="t"/>
</v:shapetype><v:shape id="_x0000_i1026" type="#_x0000_t75" style='width:191.25pt;
 height:275.25pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="index_files/image001.png" o:title=""/>
</v:shape></span><span style='font-size:14.0pt;mso-ansi-language:EN-US'><o:p></o:p></span></p>

<p class=MsoNormal style='text-align:justify;line-height:normal'><span
style='font-size:14.0pt;mso-ansi-language:EN-US'><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal style='margin-bottom:0in;text-align:justify;line-height:
normal'><b><span style='font-size:14.0pt;mso-ansi-language:EN-US'>Before
running the classifier, you have to install some additional Python packages:</span></b><span
style='font-size:14.0pt;mso-ansi-language:EN-US'> <o:p></o:p></span></p>

<p class=MsoNormal style='margin-bottom:0in;text-align:justify;line-height:
normal'><span style='font-size:14.0pt;mso-ansi-language:EN-US'>Since we are
using Anaconda environment including Spyder (Python editor), then we add
packages through Anaconda Prompt terminal:<o:p></o:p></span></p>

<p class=MsoNormal style='margin-bottom:0in;text-align:justify;line-height:
normal'><span lang=FR style='font-size:14.0pt;mso-fareast-language:FR;
mso-no-proof:yes'><v:shape id="Image_x0020_1" o:spid="_x0000_i1025" type="#_x0000_t75"
 style='width:390.75pt;height:219.75pt;visibility:visible;mso-wrap-style:square'>
 <v:imagedata src="index_files/image002.png" o:title=""/>
</v:shape></span><span style='font-size:14.0pt;mso-ansi-language:EN-US'><o:p></o:p></span></p>

<p class=MsoNormal style='margin-bottom:0in;text-align:justify;line-height:
normal'><span style='font-size:14.0pt;mso-ansi-language:EN-US'><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal style='margin-bottom:0in;text-align:justify;line-height:
normal'><span style='font-size:14.0pt;mso-ansi-language:EN-US'>For the first
time, check the already installed packages with:<o:p></o:p></span></p>

<p class=MsoNormal style='margin-bottom:0in;text-align:justify;line-height:
normal'><span style='font-size:14.0pt;mso-ansi-language:EN-US'>C:\...&gt;<span
style='background:yellow;mso-highlight:yellow'>pip list</span><o:p></o:p></span></p>

<p class=MsoNormal style='margin-bottom:0in;text-align:justify;line-height:
normal'><span style='font-size:14.0pt;mso-ansi-language:EN-US'><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal style='margin-bottom:0in;text-align:justify;line-height:
normal'><span style='font-size:14.0pt;mso-ansi-language:EN-US'><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal style='margin-bottom:0in;text-align:justify;line-height:
normal'><span style='font-size:14.0pt;mso-ansi-language:EN-US'>For BERT
embedding, you have to install:<o:p></o:p></span></p>

<p class=MsoNormal style='margin-bottom:0in;text-align:justify;line-height:
normal'><span style='font-size:14.0pt;mso-ansi-language:EN-US'>For Arabic
language:<o:p></o:p></span></p>

<p class=MsoNormal style='margin-bottom:0in;text-align:justify;line-height:
normal'><span style='font-size:14.0pt;mso-ansi-language:EN-US'>C:\...&gt;<span
style='background:lime;mso-highlight:lime'>pip install -U tensorflow</span><o:p></o:p></span></p>

<p class=MsoNormal style='margin-bottom:0in;text-align:justify;line-height:
normal'><span style='font-size:14.0pt;mso-ansi-language:EN-US'>C:\...&gt;<span
style='background:lime;mso-highlight:lime'>pip install -U transformers</span><o:p></o:p></span></p>

<p class=MsoNormal style='margin-bottom:0in;text-align:justify;line-height:
normal'><span style='font-size:14.0pt;mso-ansi-language:EN-US'>Look at (</span><span
lang=FR><a href="https://pytorch.org/get-started/locally/"><span lang=EN-US
style='font-size:14.0pt;mso-ansi-language:EN-US'>https://pytorch.org/get-started/locally/</span></a></span><span
style='font-size:14.0pt;mso-ansi-language:EN-US'>) to install pytorch<o:p></o:p></span></p>

<p class=MsoNormal style='margin-bottom:0in;text-align:justify;line-height:
normal'><span style='font-size:14.0pt;mso-ansi-language:EN-US'>C:\...&gt;<span
style='background:lime;mso-highlight:lime'>conda install pytorch torchvision
torchaudio cudatoolkit=10.2 -c pytorch<o:p></o:p></span></span></p>

<p class=MsoNormal style='margin-bottom:0in;text-align:justify;line-height:
normal'><span style='font-size:14.0pt;mso-ansi-language:EN-US'><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal style='margin-bottom:0in;text-align:justify;line-height:
normal'><span style='font-size:14.0pt;mso-ansi-language:EN-US'><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal style='margin-bottom:0in;text-align:justify;line-height:
normal'><span style='font-size:14.0pt;mso-ansi-language:EN-US'><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal style='text-align:justify;line-height:normal'><b><span
style='font-size:14.0pt;mso-ansi-language:EN-US'>Next, you will find the Python
classifier source code:<o:p></o:p></span></b></p>

<p class=MsoNormal style='text-align:justify;line-height:normal'><span
style='font-size:14.0pt;mso-ansi-language:EN-US'><a
href="ARBERT-NN_Functional_Global.py">ARBERT-NN_Functional_Global.py</a><o:p></o:p></span></p>

<p class=MsoNormal style='text-align:justify;line-height:normal'><span
style='font-size:14.0pt;mso-ansi-language:EN-US'><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal style='text-align:justify;line-height:normal'><span
style='font-size:14.0pt;mso-ansi-language:EN-US'><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal style='text-align:justify;line-height:normal'><b><span
style='font-size:14.0pt;mso-ansi-language:EN-US'>Next are some error and
warning messages that you may meet when dealing with our classifier:<o:p></o:p></span></b></p>

<div style='mso-element:para-border-div;border:none;border-bottom:solid windowtext 1.0pt;
mso-border-bottom-alt:solid windowtext .75pt;padding:0in 0in 1.0pt 0in'>

<p class=MsoNormal style='margin-bottom:0in;text-align:justify;line-height:
normal;border:none;mso-border-bottom-alt:solid windowtext .75pt;padding:0in;
mso-padding-alt:0in 0in 1.0pt 0in'><span style='font-size:14.0pt;mso-ansi-language:
EN-US'><o:p>&nbsp;</o:p></span></p>

</div>

<p class=MsoNormal style='margin-bottom:0in;text-align:justify;line-height:
normal'><span style='font-size:14.0pt;mso-ansi-language:EN-US'><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal style='margin-bottom:0in;text-align:justify;line-height:
normal'><span style='font-size:14.0pt;mso-ansi-language:EN-US'>When launching
the Arabic BERT model, if you get the following error message:<o:p></o:p></span></p>

<p class=MsoNormal style='margin-top:0in;margin-right:0in;margin-bottom:0in;
margin-left:21.25pt;text-align:justify;line-height:normal'><span
style='font-size:14.0pt;background:yellow;mso-highlight:yellow;mso-ansi-language:
EN-US'>RuntimeError: The size of tensor a (532) must match the size of tensor b
(512) at non-singleton dimension 1<o:p></o:p></span></p>

<div style='mso-element:para-border-div;border:none;border-bottom:solid windowtext 1.0pt;
mso-border-bottom-alt:solid windowtext .75pt;padding:0in 0in 1.0pt 0in'>

<p class=MsoNormal style='margin-bottom:0in;text-align:justify;line-height:
normal;border:none;mso-border-bottom-alt:solid windowtext .75pt;padding:0in;
mso-padding-alt:0in 0in 1.0pt 0in'><span style='font-size:14.0pt;mso-ansi-language:
EN-US'><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal style='margin-bottom:0in;text-align:justify;line-height:
normal;border:none;mso-border-bottom-alt:solid windowtext .75pt;padding:0in;
mso-padding-alt:0in 0in 1.0pt 0in'><span style='font-size:14.0pt;mso-ansi-language:
EN-US'>So, you must reduce the string length introduced to the BERT model. For
example: <span style='background:yellow;mso-highlight:yellow'>Arabic_Bert_Model_T(i[0:2000])</span><o:p></o:p></span></p>

<p class=MsoNormal style='margin-bottom:0in;text-align:justify;line-height:
normal;border:none;mso-border-bottom-alt:solid windowtext .75pt;padding:0in;
mso-padding-alt:0in 0in 1.0pt 0in'><span style='font-size:14.0pt;mso-ansi-language:
EN-US'><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal style='margin-bottom:0in;text-align:justify;line-height:
normal;border:none;mso-border-bottom-alt:solid windowtext .75pt;padding:0in;
mso-padding-alt:0in 0in 1.0pt 0in'><span style='font-size:14.0pt;mso-ansi-language:
EN-US'><o:p>&nbsp;</o:p></span></p>

</div>

<p class=MsoNormal style='margin-top:0in;margin-right:0in;margin-bottom:0in;
margin-left:21.25pt;text-align:justify;line-height:normal'><span
style='font-size:14.0pt;background:darkblue;mso-highlight:darkblue;mso-ansi-language:
EN-US'><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal style='margin-bottom:0in;text-align:justify;line-height:
normal'><span style='font-size:14.0pt;mso-ansi-language:EN-US'>If you receive
the following error message:<o:p></o:p></span></p>

<p class=MsoNormal style='margin-top:0in;margin-right:0in;margin-bottom:0in;
margin-left:21.25pt;text-align:justify;line-height:normal'><span
style='font-size:14.0pt;background:yellow;mso-highlight:yellow;mso-ansi-language:
EN-US'>ValueError: The first argument to `Layer.call` must always be passed.<o:p></o:p></span></p>

<div style='mso-element:para-border-div;border:none;border-bottom:solid windowtext 1.0pt;
mso-border-bottom-alt:solid windowtext .75pt;padding:0in 0in 1.0pt 0in'>

<p class=MsoNormal style='margin-bottom:0in;text-align:justify;line-height:
normal;border:none;mso-border-bottom-alt:solid windowtext .75pt;padding:0in;
mso-padding-alt:0in 0in 1.0pt 0in'><span style='font-size:14.0pt;mso-ansi-language:
EN-US'><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal style='margin-bottom:0in;text-align:justify;line-height:
normal;border:none;mso-border-bottom-alt:solid windowtext .75pt;padding:0in;
mso-padding-alt:0in 0in 1.0pt 0in'><span style='font-size:14.0pt;mso-ansi-language:
EN-US'>This means that the BERT model must be launched before building the
Neural Network model.<o:p></o:p></span></p>

<p class=MsoNormal style='margin-bottom:0in;text-align:justify;line-height:
normal;border:none;mso-border-bottom-alt:solid windowtext .75pt;padding:0in;
mso-padding-alt:0in 0in 1.0pt 0in'><span style='font-size:14.0pt;mso-ansi-language:
EN-US'><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal style='margin-bottom:0in;text-align:justify;line-height:
normal;border:none;mso-border-bottom-alt:solid windowtext .75pt;padding:0in;
mso-padding-alt:0in 0in 1.0pt 0in'><span style='font-size:14.0pt;mso-ansi-language:
EN-US'><o:p>&nbsp;</o:p></span></p>

</div>

</div>

</body>

</html>
