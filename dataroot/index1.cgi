
sub CHILRANG_INDEX {
	print <<"EOM";






<STYLE>BODY {
	CURSOR: url('samnet.cur')
}
A {
	CURSOR: url('samnet.ani'); TEXT-DECORATION: none
}
</STYLE>
<BODY oncontextmenu="return false" onselectstart="return false" ondragstart="return false" bgcolor="black" leftmargin="0" marginwidth="0" topmargin="0" marginheight="0">
<body bgcolor="white" text="black" link="blue" vlink="purple" alink="red" leftmargin="0" marginwidth="0" topmargin="0" marginheight="0" background="$IMG//back.jpg">
<table align="center" cellpadding="0" cellspacing="0" width="950">
    <tr>
        <td width="950" height="73" colspan="4">
            <p><img src="$IMG/up.gif" width="950" height="93" border="0"></p>
        </td>
    </tr>
    <tr>
        <td width="10" height="609" rowspan="5">
            <p></p>
        </td>
        <td width="408" height="14" background="$IMG/backg1.gif">
            <p align="center"><font face="����" color="#FFCC00"><span style="font-size:9pt;"><b>[$new_date]</b> ����
            �ϱ��� ������ <B>$next_time</B>�� ���ҽ��ϴ�.</span></font></p>
        </td>
        <td width="512" height="14" colspan="2">
            <table cellpadding="0" cellspacing="0" width="512">
		<form action="$FILE_STATUS" method="GET"><input type="hidden" name="mode" value="STATUS">
                <tr>
                    <td width="79">
                        <p><img src="$IMG/id.gif" width="79" height="28" border="0"></p>
                    </td>
                    <td width="124" background="$IMG/backg2.gif">
                        <p align="center"><input type="text" name="id" size="17" style="font-family:�ü�; color:rgb(222,195,61); text-decoration:none; background-color:rgb(41,77,90); border-style:none;" value="$_id">
                    </td>
                    <td width="79">
                        <p><img src="$IMG/pw.gif" width="79" height="28" border="0"></p>
                    </td>
                    <td width="124" background="$IMG/backg2.gif">
                        <p align="center"><input type="password" name="pass" size="17" style="font-family:�ü�; color:rgb(222,195,61); background-color:rgb(41,77,90); border-style:none;" value="$_pass">
                    </td>
                    <td width="106" background="$IMG/backg3.gif">
                        <p align="center"><input type="submit" style="font-family:�ü�; color:rgb(204,255,0); background-color:rgb(41,77,90); border-style:none;" value="���Ӱ���"></form></p>

                    </td>
                </tr>
            </table>
        </td>
    </tr>
    <tr>
        <td width="408" height="284"  background="$IMG/backg.gif" rowspan="2">
            <p>
      <TABLE bgcolor=$TD_C2 width=108% height="315" cellpadding="0" cellspacing="0">
	<center>
        <TBODY>
          <TR>
            <TD width=20 bgcolor=$TD_C2></TD>
EOM
	open(IN,"$TOWN_LIST") or &ERR("������ ������ ������ �ʽ��ϴ�.");
	@TOWN_DATA = <IN>;
	close(IN);

    for($i=1;$i<13;$i++){
		print "<TD width=20 bgcolor=$TD_C1><center>$i</TD>";
	}
	print "</TR>";
     for($i=0;$i<12;$i++){
		$n = $i+1;
		print "<TR><TD bgcolor=$TD_C3><center>$n</td>";
		for($j=0;$j<12;$j++){
				$m_hit=0;$zx=0;
				foreach(@TOWN_DATA){
					($zzname,$zzcon,$zznum,$zznou,$zzsyo,$zzshiro,$zznou_max,$zzsyo_max,$zzshiro_max,$zzpri,$zzx,$zzy)=split(/<>/);
					if("$zzx" eq "$j" && "$zzy" eq "$i"){$m_hit=1;last;}
					$zx++;
				}
				$col="";
				if($m_hit){
					if($zzname eq "����" || $zzname eq "���" || $zzname eq "���" || $zzname eq "����" || $zzname eq "��" || $zzname eq "��â" || $zzname eq "�Ǿ�" || $zzname eq "��"){
						print "<TH bgcolor=$ELE_BG[$cou_ele[$zzcon]]><img src=$IMG/bg3.gif width=20 height=20 border=0 alt=$zzname��$cou_name[$zzcon]��></TH>";
					}elsif($zzname eq "ȫ��" || $zzname eq "��" || $zzname eq "����" || $zzname eq "����" || $zzname eq "����" || $zzname eq "����" || $zzname eq "��" || $zzname eq "����" || $zzname eq "����" || $zzname eq "�Ϻ�" || $zzname eq "����" || $zzname eq "��" || $zzname eq "����"){
						print "<TH bgcolor=$ELE_BG[$cou_ele[$zzcon]]><img src=$IMG/bg2.gif width=20 height=20 border=0 alt=$zzname��$cou_name[$zzcon]��></TH>";
					}elsif($zzname eq "����" || $zzname eq "õ��" || $zzname eq "���" || $zzname eq "����" || $zzname eq "����" || $zzname eq "����" || $zzname eq "����" || $zzname eq "���" || $zzname eq "����" || $zzname eq "����" || $zzname eq "�û�" || $zzname eq "��" || $zzname eq "�ܾ�" || $zzname eq "����" || $zzname eq "ȸ��" || $zzname eq "�����" || $zzname eq "���"){
						print "<TH bgcolor=$ELE_BG[$cou_ele[$zzcon]]><img src=$IMG/bg1.gif width=20 height=20 border=0 alt=$zzname��$cou_name[$zzcon]��></TH>";
					}elsif($zzname eq "1"){
						print "<TH img background=$IMG/sea.gif></TH>";
					}elsif($zzname eq "2"){
						print "<TH img background=$IMG/san.gif></TH>";
					}elsif($zzname eq "3"){
						print "<TH img background=$IMG/san1.gif></TH>";
					}elsif($zzname eq "4"){
						print "<TH img background=$IMG/hwang.gif></TH>";
					}elsif($zzname eq "5"){
						print "<TH img background=$IMG/cho.gif></TH>";
					}else{
						print "<TH bgcolor=$ELE_BG[$cou_ele[$zzcon]]><img src=$IMG/bg0.gif width=20 height=20 border=0 alt=$zzname��$cou_name[$zzcon]��></TH>";
					}
				}else{
					print "<TH> </TH>";
				}
		}
		print "</TR>";
	}
print <<"EOM";
        </TBODY>
      </TABLE>
</p>
        </td>
        <td width="502" height="14" >
            <p><img src="$IMG/menu1.gif" width="502" height="20" border="0"></p>
        </td>
        <td width="10" height="581" rowspan="4">
            <p></p>
        </td>
    </tr>
    <tr>
        <td width="502" height="270" background="$IMG/backg.gif">
            <p>$S_MES</p>
        </td>
    </tr>
    <tr>
        <td width="502" height="291" background="$IMG/backg.gif" rowspan="2">

            <table align="center" cellpadding="0" cellspacing="0" width="431">
                <tr>
                    <td width="431" height="12" colspan="3">
                    </td>
                </tr>
                <tr>
                    <td width="431" height="72" colspan="3" background="$IMG/menu0.gif">
$G_MES
                    </td>
                </tr>
                <tr>
                    <td width="431" height="12" colspan="3">

                    </td>
                </tr>
                <tr>
                    <td width="33%" height="97">
                        <p align="center"><a href="./entry.cgi" title="�ﱹ�� �������� NET - ĥ�������� �ű԰����� �մϴ�."><img src="$IMG/m1.jpg" width="130" height="90" border="0"></a></p>
                    </td>
                    <td width="33%" height="97">
                        <p align="center"><a href="./ranking.cgi" title="���� ���� ��� ����� ������ �϶��մϴ�."><img src="$IMG/m2.jpg" width="130" height="90" border="0"></a></p>
                    </td>
                    <td width="33%" height="97"><p align="center"><a href="./ranking2.cgi" title="�� �ɷ�ġ �κ� 1~10������ �϶��մϴ�."><img src="$IMG/m3.jpg" width="130" height="90" border="0"></a></p>
                    </td>
                </tr>
                <tr>
                    <td width="33%" height="110">
                        <p align="center"><a href="./manual.htm" title="ĥ�������� �÷��� �޴����Դϴ�."><img src="$IMG/m4.jpg" width="130" height="90" border="0"></a></p>
                    </td>
                    <td width="33%" height="110">
                        <p align="center"><a href="./sagwan.htm" title="���� ������ ������� �϶��մϴ�."><img src="$IMG/m5.jpg" width="130" height="90" border="0"></a></p>
                    </td>
                    <td width="33%" height="110">
                        <p align="center"><a href="http://cafe.naver.com/120sam" target="_blank" title="ĥ�������� ����ī���Դϴ�."><img src="$IMG/m6.jpg" width="130" height="90" border="0"></a></p>
                    </td>
                </tr>
            </table>

        </td>
        <td width="502" height="13">
            <p><img src="$IMG/menu2.gif" width="502" height="20" border="0"></p>
        </td>
    </tr>
    <tr>
        <td width="502" height="278" background="$IMG/backg.gif">
            <p>$D_MES</p>
        </td>
    </tr>
    <tr>
        <td width="950" colspan="4">
            <p><img src="$IMG/down.gif" width="950" height="26" border="0"></p>
        </td>
    </tr>
</table>
</body>
EOM
}
1;
