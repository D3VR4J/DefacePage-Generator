#!Creaated by D3VR4J in learning process
import os


run = True
while run:
      fname = input("Input Your Deface Page Name: ")
      fname = f"./{fname}.htm"
      if os.path.isfile(fname) and os.stat(fname).st_size != 0:
         print ("Already Present in the directory")
         continue
      else:


           fname = open(fname, "w+")
           #inputs
           alert = input("Input Alert Message:")
           yname = input("Input Your Name: ")
           logolink = input("Input your logo link: ")

           cursor = input("Want to put Cursor?(yes/no): ")
           if cursor == "yes" or cursor == "Yes" or cursor == "Y" or cursor == "y":
              cursor = input("Input your cursor link.")
           else:
                cursor = f"https://i.ibb.co/rf5fvxx/D3-VR4-J-cursor.png"

           victim = input("Input Victim/Enemies Name: ")
           msg1 = input("Input Message 1: ")
           msg2 = input("Input Message 2: ")

           tname = input("Want to put your Team Name?(yes/no): ")
           if tname == "yes" or tname == "Yes" or tname == "Y" or tname == "y":
              tname = input("Input Your Team name: ")
           else:
                tname = f""

           profile = input("Input Your Profile Link: ")


           #webpage
           defacepage = f"""
           <!DOCTYPE html>
        <html>
        <head>
        <SCRIPT> alert("{alert}")</SCRIPT>
        <title>•{yname} IS HERE•</title>
        <style>
        body {{
        background: url(https://media.tumblr.com/c838dd887608a325eaae477ffa4dd2b7/tumblr_myrxsem7AC1s8tqb9o1_500.gif) no-repeat center center fixed;
          -webkit-background-size: cover;
          -moz-background-size: cover;
          -o-background-size: cover;
          background-size: cover;
        font-family:Cookie,sans-serif;
        }}
        </style>
        <meta charset="UTF-8">

        	<meta name="copyright" content="3"/>
        	<meta name="description" content="{yname} Was Here "/>
        <meta http-equiv="content-type" content="text/html; charset=ISO-8859-1">
        <meta name="robots" content="index,follow">
        <meta name="googlebot" content="index,follow">
         <link rel="shortcut icon" href="{logolink}">




         <script type='text/javascript'>
                var DADrightclicktheme = 'Dark';
                var DADrightclickimage = '{logolink}';

               </script>


              <style type='text/css'>body, a, a:link{{cursor:url({cursor}), default;}} a:hover {{cursor:url({cursor}),wait;}}</style>




        <script src="https://html5shiv.googlecode.com/svn/trunk/html5.js"></script>
        <STYLE>
        a:hover
        {{filter:progid:DXImageTransform.Microsoft.Glow(Color=#FF0000, Strength=5);width:100%;}}

        </STYLE>

        <style>
        body{{text-alignfont-family: 'BatmanForeverAlternate', cursive;}}
        hr{{border: 1px solid #1C1C1C;}}
        </style>
        <style type="text/css">
        body,td,th {{
        color: #000000;
        }}
        body {{background-color: #000000;
        }}
        a {{ text-decoration:none; }}
        a:link {{ color: #00FF00}}
        a:visited {{ color: #00FF00}}
        a:hover {{ color: #00FF00}}
        a:active {{ color: #00FF00}}




        .style1 {{
        text-align: center;
        }}



        * {{
        padding:0;
        margin:0;
        }}



        * {{
        padding:0;
        margin:0;
        }}



        *{{padding: 0px;margin: 0px;}}



        .style98 {{
        font-family: "Courier New";
        color: white;
        }}



        .auto-style1 {{
        Helvetica, BatmanForeverAlternate;
        font-weight: bold;
        font-size: 15px;
        color: #FFFFFF;
        }}
        <font size="5px" style="font-family: Iceland, BatmanForeverAlternate ;color:defult;text-shadow: 0 0 3px red, 0px 0px 5px red" >


        </style>
        <center><embed src="https://www.youtube.com/v/bHKiQFJllvU&autoplay=1" type="application/x-shockwave-flash" wmode="transparent" width="1" height="1" /></embed>
        <marquee scrolldelay="3"><font size="15" color="green"><blink> Your Website Has Been </blink></font><font size="15" color="red"><blink> Hacked By {yname} </blink></font></marquee>
        <meta http-equiv="Content-Language" content="en-us">
        <meta http-equiv="Content-Type" content="text/html; charset=windows-1252">
        </head>

        <body bgcolor=black oncontextmenu="return false;" onkeydown="return false;" onload="teclear();" onmousedown="return false;">

        <center><img border="0" height="300" src="{logolink}" width="300" /></td></center>
            <script language="JavaScript">
            var numraindrops="150";
            var speed="5";
            var rainsize="2";
            var wind="left";
            var genxgallery="";

            function tb5_makeArray(n){{ this.length = n; return this.length;
            }}
            tb5_messages = new tb5_makeArray(2);
            tb5_messages[0] = " ~{yname}~ ";
            tb5_messages[1] = " ~{yname}~ ";
            tb5_rptType = 'infinite';
            tb5_rptNbr = 10;
            tb5_speed = 1;
            tb5_delay = 10000;
            var tb5_counter=1;
            var tb5_currMsg=0;
            var tb5_stsmsg="";
            function tb5_shuffle(arr){{
            var k;
            for (i=0; i<arr.length; i++){{ k = Math.round(Math.random() * (arr.length - i - 1)) + i; temp = arr[i];arr[i]=arr[k];arr[k]=temp;
            }}
            return arr;
            }}
            tb5_arr = new tb5_makeArray(tb5_messages[tb5_currMsg].length);
            tb5_sts = new tb5_makeArray(tb5_messages[tb5_currMsg].length);
            for (var i=0; i<tb5_messages[tb5_currMsg].length; i++){{ tb5_arr[i] = i; tb5_sts[i] = "_";
            }}
            tb5_arr = tb5_shuffle(tb5_arr);
            function tb5_init(n){{
            var k;
            if (n == tb5_arr.length){{ if (tb5_currMsg == tb5_messages.length-1){{ if ((tb5_rptType == 'finite') && (tb5_counter==tb5_rptNbr)){{ clearTimeout(tb5_timerID); return; }} tb5_counter++; tb5_currMsg=0; }} else{{ tb5_currMsg++; }} n=0; tb5_arr = new tb5_makeArray(tb5_messages[tb5_currMsg].length); tb5_sts = new tb5_makeArray(tb5_messages[tb5_currMsg].length); for (var i=0; i<tb5_messages[tb5_currMsg].length; i++){{ tb5_arr[i] = i; tb5_sts[i] = "_"; }} tb5_arr = tb5_shuffle(tb5_arr); tb5_sp=tb5_delay;
            }}
            else{{ tb5_sp=tb5_speed; k = tb5_arr[n]; tb5_sts[k] = tb5_messages[tb5_currMsg].charAt(k); tb5_stsmsg = ""; for (var i=0; i<tb5_sts.length; i++) tb5_stsmsg += tb5_sts[i]; document.title = tb5_stsmsg; n++; }} tb5_timerID = setTimeout("tb5_init("+n+")", tb5_sp);
            }}
            function tb5_randomizetitle(){{ tb5_init(0);
            }}
            tb5_randomizetitle();



           </script>
             <script>
        var message=" Java Skid Protecter || Enemy~";
        ///////////////////////////////////
        function clickIE4(){{if (event.button==2){{alert(message);return false;}}}}
        function clickNS4(e){{if (document.layers||document.getElementById&&!document.all){{if (e.which==2||e.which==3){{alert(message);return false;}}}}}}
        if (document.layers){{document.captureEvents(Event.MOUSEDOWN);document.onmousedown=clickNS4;}}
        else if (document.all&&!document.getElementById){{document.onmousedown=clickIE4;}}
        document.oncontextmenu=new Function("alert(message);return false")
        </script>
        <body style="background-color:#000000;background> <br><br><!--
            </body></html><br>
            <script language="JavaScript1.2">


            <div align="center"><table border="0" width="70%"><tr><td>

            <h1><font face="Enemy"><center><SCRIPT>



            farbbibliothek = new Array();



            farbbibliothek[0] = new Array("#FF0000","#FF1100","#FF2200","#FF3300","#FF4400","#FF5500","#FF6600","#FF7700","#FF8800","#FF9900","#FFaa00","#FFbb00","#FFcc00","#FFdd00","#FFee00","#FFff00","#FFee00","#FFdd00","#FFcc00","#FFbb00","#FFaa00","#FF9900","#FF8800","#FF7700","#FF6600","#FF5500","#FF4400","#FF3300","#FF2200","#FF1100");



            farbbibliothek[1] = new Array("#FF0000","#FFFFFF","#FFFFFF","#FF0000");



            farbbibliothek[2] = new Array("#FFFFFF","#FF0000","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF");



            farbbibliothek[3] = new Array("#FF0000","#FF4000","#FF8000","#FFC000","#FFFF00","#C0FF00","#80FF00","#40FF00","#00FF00","#00FF40","#00FF80","#00FFC0","#00FFFF","#00C0FF","#0080FF","#0040FF","#0000FF","#4000FF","#8000FF","#C000FF","#FF00FF","#FF00C0","#FF0080","#FF0040");



            farbbibliothek[4] = new Array("#FF0000","#EE0000","#DD0000","#CC0000","#BB0000","#AA0000","#990000","#880000","#770000","#660000","#550000","#440000","#330000","#220000","#110000","#000000","#110000","#220000","#330000","#440000","#550000","#660000","#770000","#880000","#990000","#AA0000","#BB0000","#CC0000","#DD0000","#EE0000");


            farbbibliothek[5] = new Array("#FF0000","#FF0000","#FF0000","#FFFFFF","#FFFFFF","#FFFFFF");


            farbbibliothek[6] = new Array("#FF0000","#FDF5E6");



            farben = farbbibliothek[4];



            function farbschrift()



            {{



            for(var i=0 ; i<Buchstabe.length; i++)



            {{



            document.all["a"+i].style.color=farben[i];



            }}



            farbverlauf();



            }}



            function string2array(text)



            {{



            Buchstabe = new Array();



            while(farben.length<text.length)



            {{



            farben = farben.concat(farben);



            }}



            k=0;



            while(k<=text.length)



            {{



            Buchstabe[k] = text.charAt(k);



            k++;



            }}



            }}



            function divserzeugen()



            {{



            for(var i=0 ; i<Buchstabe.length; i++)



            {{



            document.write("<span id='a"+i+"' class='a"+i+"'>"+Buchstabe[i] + "</span>");



            }}



            farbschrift();



            }}



            var a=1;



            function farbverlauf()



            {{



            for(var i=0 ; i<farben.length; i++)



            {{



            farben[i-1]=farben[i];



            }}



            farben[farben.length-1]=farben[-1];







            setTimeout("farbschrift()",30);



            }}



            //



            var farbsatz=1;



            function farbtauscher()



            {{



            farben = farbbibliothek[farbsatz];



            while(farben.length<text.length)



            {{



            farben = farben.concat(farben);



            }}



            farbsatz=Math.floor(Math.random()*(farbbibliothek.length-0.0001));



            }}



            setInterval("farbtauscher()",10000);



            text ="Your Website Has Been Hacked";//h



            string2array(text);



            divserzeugen();



            //document.write(text);
            </SCRIPT></center></h1></font>
              <SCRIPT LANGUAGE="JavaScript">
                <!-- Disable




                function disableselect(e) {{




                    return false




                }}




                function reEnable() {{




                    return true




                }}




                //if IE4+




                document.onselectstart = new Function("return false")




                document.oncontextmenu = new Function("return false")




                //if NS6




                if (window.sidebar) {{




                    document.onmousedown = disableselect




                    document.onclick = reEnable




                }}




                //-->
            </script>

        	<style type="text/css">
        /* Circle Text Styles */
        #outerCircleText {{
        /* Optional - DO NOT SET FONT-SIZE HERE, SET IT IN THE SCRIPT */
        font-style: italic;
        font-weight: bold;
        font-family: 'comic sans ms', verdana, arial;
        color:#bc0074;
        /* End Optional */

        /* Start Required - Do Not Edit */
        position: absolute;top: 0;left: 0;z-index: 3000;cursor: default;}}
        #outerCircleText div {{position: relative;}}
        #outerCircleText div div {{position: absolute;top: 0;left: 0;text-align: center;}}
        /* End Required */
        /* End Circle Text Styles */
        </style>


        <script type="text/javascript">
        ;(function(){{


        var msg = "{yname}";
        var size = 23;
        var circleY = 0.75; var circleX = 2;
        var letter_spacing = 5;
        var diameter = 10;
        var rotation = 0.4;
        var speed = 0.3;

        ////////////////////// Stop Editing //////////////////////

        if (!window.addEventListener && !window.attachEvent || !document.createElement) return;

        msg = msg.split('');
        var n = msg.length - 1, a = Math.round(size * diameter * 0.208333), currStep = 20,
        ymouse = a * circleY + 20, xmouse = a * circleX + 20, y = [], x = [], Y = [], X = [],
        o = document.createElement('div'), oi = document.createElement('div'),
        b = document.compatMode && document.compatMode != "BackCompat"? document.documentElement : document.body,

        mouse = function(e){{
         e = e || window.event;
         ymouse = !isNaN(e.pageY)? e.pageY : e.clientY; // y-position
         xmouse = !isNaN(e.pageX)? e.pageX : e.clientX; // x-position
        }},

        makecircle = function(){{ // rotation/positioning
         if(init.nopy){{
          o.style.top = (b || document.body).scrollTop + 'px';
          o.style.left = (b || document.body).scrollLeft + 'px';
         }};
         currStep -= rotation;
         for (var d, i = n; i > -1; --i){{ // makes the circle
          d = document.getElementById('iemsg' + i).style;
          d.top = Math.round(y[i] + a * Math.sin((currStep + i) / letter_spacing) * circleY - 15) + 'px';
          d.left = Math.round(x[i] + a * Math.cos((currStep + i) / letter_spacing) * circleX) + 'px';
         }};
        }},

        drag = function(){{ // makes the resistance
         y[0] = Y[0] += (ymouse - Y[0]) * speed;
         x[0] = X[0] += (xmouse - 20 - X[0]) * speed;
         for (var i = n; i > 0; --i){{
          y[i] = Y[i] += (y[i-1] - Y[i]) * speed;
          x[i] = X[i] += (x[i-1] - X[i]) * speed;
         }};
         makecircle();
        }},

        init = function(){{ // appends message divs, & sets initial values for positioning arrays
         if(!isNaN(window.pageYOffset)){{
          ymouse += window.pageYOffset;
          xmouse += window.pageXOffset;
         }} else init.nopy = true;
         for (var d, i = n; i > -1; --i){{
          d = document.createElement('div'); d.id = 'iemsg' + i;
          d.style.height = d.style.width = a + 'px';
          d.appendChild(document.createTextNode(msg[i]));
          oi.appendChild(d); y[i] = x[i] = Y[i] = X[i] = 0;
         }};
         o.appendChild(oi); document.body.appendChild(o);
         setInterval(drag, 25);
        }},

        ascroll = function(){{
         ymouse += window.pageYOffset;
         xmouse += window.pageXOffset;
         window.removeEventListener('scroll', ascroll, false);
        }};

        o.id = 'outerCircleText'; o.style.fontSize = size + 'px';

        if (window.addEventListener){{
         window.addEventListener('load', init, false);
         document.addEventListener('mouseover', mouse, false);
         document.addEventListener('mousemove', mouse, false);
          if (/Apple/.test(navigator.vendor))
           window.addEventListener('scroll', ascroll, false);
        }}
        else if (window.attachEvent){{
         window.attachEvent('onload', init);
         document.attachEvent('onmousemove', mouse);
        }};

        }})();

        </script>
        <center><font face="Iceland" style="color:#0ba544;text-shadow:0px 1px 5px #000;font-size:30px">"Hello <font face="Iceland" style="color:#a50b0b;text-shadow:0px 1px 5px #000;font-size:30px">{victim}"</center></font>
        <p align="center" dir="ltr"><font size="5" color="white">{msg1}




        <p align="center" dir="ltr"><font size="5" color="#58FAF4">{msg2}

        <center><font face="Comic Sans MS" size="4" color="green">-: WE ARE :- <br><font face="Comic Sans MS" size="4" color="orange">{tname}
              </font><br><center><font face="Comic Sans MS" size="4" color="white">follow us ></font><a href="{logolink}">facebook</a></center><br><font face="Comic Sans MS" size="4" color="red">| Copyright 2022.All rights Reserved |</font><font face="Comic Sans MS" size="4" color="Green"></font></center>
         <marquee behavior="alternate">
         <a href=<img src= width="60" height="100"></a>
         </marquee>
                 </body>
         </html>

        """
           print("DefacePage Created ")
           run = False
#export webpage
fname.write(defacepage)