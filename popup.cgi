#!/usr/bin/perl

require 'jcode.pl';
require './ini_file/index.ini';
require 'suport.cgi';

&DECODE;
&BODY;

sub BODY {

print <<"EOM";

<html>

<head>
<script language="JavaScript">  
function setCookie( name, value, expiredays ) 
{ 
var todayDate = new Date(); 
todayDate.setDate( todayDate.getDate() + expiredays ); 
document.cookie = name + "=" + escape( value ) + "; path=/; expires=" + todayDate.toGMTString() + ";" 
} 
 
function closeWin()  {
{ 
if ( document.cnjform.notice.checked )  // 폼네임 cnjform 은 동일해야 합니다.
setCookie("CookieName", "no" , 1);   // 부모창에서 지정한 쿠키네임과 일치 해야 합니다.
} 
top.close();
}
</script>
<meta http-equiv="content-type" content="text/html; charset=euc-kr">
<title>공지사항</title>
<meta name="generator" content="Namo WebEditor v5.0">
</head>

<body bgcolor="white" text="black" link="blue" vlink="purple" alink="red" leftmargin="0" marginwidth="0" topmargin="0" marginheight="0">
<table cellpadding="20" cellspacing="0" width="350" height="568">
    <tr>
        <td width="1101" height="218" background="event.jpg"><P align="center"><img src="title.gif" width="150" height="80" border="0"></P>
            <p><span style="font-size:9pt;">이번주 일요일 오후 8시(10/19)&nbsp;irc 채널에서 이벤트를 개최합니다.<br>진행방식은 irc 칠랑섭 채널에 모여서 주사위를 굴려 추첨하는 식으로 할 것이고&nbsp; 다른섭에서 한 유례가 있다고 하네요.<br> =ㅅ=타섭에서 해보신 분들은 아실테고 모르시는 분들을 위해 간단히 설명하면 칠랑섭채널에 모여 자기 아이디 옆에 숫자를 씁니다.<br>만약 사람이 50명도 참여 한다 그러면 50명이 1~50까지의 숫자를 나눠 갖고 갈량_ 32&nbsp; 이런식의 닉넴으로 있다가 제가 주사위를 
굴려서 만약 1~50숫자 중에 32가 나왔다 그러면 제가 당첨되는 겁니다..<br>대충 이해 하셧을듯합니다.<br>상품은 칠랑섭만의 특징인 특기포인트를 주는 방식으로 하겠습니다.<br>물론 더불어 소정의 금액도 같이 드리겠습니다.</span></p>
            <table border="1" width="249" align="center" cellspacing="0" bordercolordark="white" bordercolorlight="black">
                <tr>
                    <td width="97"><P align="center"><span style="font-size:9pt;"><b>특기포인트</b></span></P>
                    </td>
                    <td width="64">
                        <p align="center"><span style="font-size:9pt;">1000pt</span></p>
                    </td>
                    <td width="74">
                        <p align="center"><span style="font-size:9pt;">3분</span></p>
                    </td>
                </tr>
                <tr>
                    <td width="97"><P align="center"><span style="font-size:9pt;"><b>금</b></span></P>
                    </td>
                    <td width="64">
                        <p align="center"><span style="font-size:9pt;">20000전</span></p>
                    </td>
                    <td width="74">
                        <p align="center"><span style="font-size:9pt;">3분</span></p>
                    </td>
                </tr>
                <tr>
                    <td width="97"><P align="center"><span style="font-size:9pt;"><b>임의의아이템</b></span></P>
                    </td>
                    <td width="64">
                        <p align="center"><span style="font-size:9pt;">1개</span></p>
                    </td>
                    <td width="74">
                        <p align="center"><span style="font-size:9pt;">1분</span></p>
                    </td>
                </tr>
            </table>
<P><span style="font-size:9pt;"><font color="red"><b>20명이상일 시에만 유효하니 많은 참여 부탁드립니다.</b></font></span><form name="cnjform"> 
                <p align="center"><span style="font-size:9pt;"><input type="checkbox" name="notice" onclick="closeWin()"> 오늘 하룻동안 페이지를 열지 않습니다.</span> 
</form>
        </td>
    </tr>
</table>
</body>

</html>

EOM

}

