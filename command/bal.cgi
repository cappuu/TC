sub BAL {

	if($in{'no'} eq ""){&ERR("NO:�� �Էµ��� �ʾҽ��ϴ�.");}
	&CHARA_MAIN_OPEN;
	&CHARA_ITEM_OPEN;
	&TOWN_DATA_OPEN("$kpos");
	&COUNTRY_DATA_OPEN($kcon);
	&TIME_DATA;

	$comlist = 67;

	$no = $in{'no'} + 1;
	foreach(@no){
		$no_list .= "<input type=hidden name=no value=$_>"
	}

	&HEADER;

	print <<"EOM";
<STYLE>BODY {
	CURSOR: url('samnet.cur')
}
A {
	CURSOR: url('samnet.ani'); TEXT-DECORATION: none
}
</STYLE>
<BODY oncontextmenu="return false" onselectstart="return false" ondragstart="return false">
<body leftmargin="0" marginwidth="0" topmargin="0" marginheight="0">
<table align="center" width="950">
    <tr>
        <td>
            <img src="$IMG/up.gif">
        </td>
    </tr>
    <tr height="600">
        <td background="$IMG/backg.gif">
<table align="center" border="1" cellspacing="0" width="752" height="492" bordercolordark="white" bordercolorlight="black">
    <tr>
        <td width="1101" height="492" background="$IMG/cola.jpg">
            <table cellpadding="0" cellspacing="0" width="752" height="488" bordercolordark="white" bordercolorlight="black">
                <tr>
                    <td width="752" height="22" colspan="8">
                        <p>&nbsp;</p>
                    </td>
                </tr>
                <tr>
                    <td width="11" height="467" rowspan="6">
                        <p>&nbsp;</p>
                    </td>
                    <td width="52" height="236" rowspan="4">
                        <p>&nbsp;</p>
                    </td>
                    <td width="141" height="236" rowspan="4">
                        <table cellpadding="0" cellspacing="0">
                            <tr>
                                <td width="131" height="18">
                                    <p><font color="white"><span style="font-size:9pt;">$cou_name[$kcon]��</span></font></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="131" height="18">
				<table cellpadding="0" cellspacing="0"><tr><td width="$kstr1" bgcolor="#006600"><font color="white"><span style="font-size:8pt;">$kstrt</span></font></td></tr></table>
                                </td>
                            </tr>
                            <tr>
                                <td width="131" height="18">
				<table cellpadding="0" cellspacing="0"><tr><td width="$kint1" bgcolor="#006600"><font color="white"><span style="font-size:8pt;">$kintt</span></font></td></tr></table>
                                </td>
                            </tr>
                            <tr>
                                <td width="131" height="18">
				<table cellpadding="0" cellspacing="0"><tr><td width="$klea1" bgcolor="#006600"><font color="white"><span style="font-size:8pt;">$kleat</span></font></td></tr></table>
                                </td>
                            </tr>
                            <tr>
                                <td width="131" height="18">
                                <table cellpadding="0" cellspacing="0"><tr><td width="$kcha1" bgcolor="#006600"><font color="white"><span style="font-size:8pt;">$kchat</span></font></td></tr></table>
                                </td>
                            </tr>
                            <tr>
                                <td width="131" height="18">
                                <table cellpadding="0" cellspacing="0"><tr><td width="$kgold1" bgcolor="#006600"><font color="white"><span style="font-size:8pt;">$kgold</span></font></td></tr></table>
                                </td>
                            </tr>
                            <tr>
                                <td width="131" height="18">
                                <table cellpadding="0" cellspacing="0"><tr><td width="$krice1" bgcolor="#006600"><font color="white"><span style="font-size:8pt;">$krice</span></font></td></tr></table>
                                </td>
                            </tr>
                            <tr>
                                <td width="131" height="18">
                                <table cellpadding="0" cellspacing="0"><tr><td width="$kcex1" bgcolor="#006600"><font color="white"><span style="font-size:8pt;">$kcex</span></font></td></tr></table>
                                </td>
                            </tr>
                            <tr>
                                <td width="131" height="18">
                                <table cellpadding="0" cellspacing="0"><tr><td width="$ksol1" bgcolor="#006600"><font color="white"><span style="font-size:8pt;">$ksol</span></font></td></tr></table>
                                </td>
                            </tr>
                            <tr>
                                <td width="131" height="18">
                                <table cellpadding="0" cellspacing="0"><tr><td width="$kgat" bgcolor="#006600"><font color="white"><span style="font-size:8pt;">$kgat</span></font></td></tr></table>
                                </td>
                            </tr>
                        </table>

                    </td>
                    <td width="25" height="236" rowspan="4">
                    </td>
                    <td width="70" height="34">
                    </td>
                    <td width="24" height="236" rowspan="4">
&nbsp;                  </td>
                    <td width="421" height="467" rowspan="6">
<TABLE border=0 width=100% height=80%><TR><TD>
<center>

</span></font>
      <TABLE bgcolor=$bg_c background="$IMG/mapbg.gif" width=96% height=5 border="0" cellspacing=0>
        <TBODY>
<TR><TH colspan= 13 bgcolor=442200><font color="white" face="����"><span style="font-size:9pt;">$new_date</font></span></TH></TR>

          <TR>
            <TD width=20 bgcolor=$TD_C2><font color="white" face="����"><span style="font-size:9pt;">-</span></font></TD>
EOM


	for($i=1;$i<13;$i++){
		print "<TD width=20 bgcolor=$TD_C1>$i</TD>";
	}
	print "</TR>";
     for($i=0;$i<12;$i++){
		$n = $i+1;
		print "<TR><TD bgcolor=$TD_C3>$n</td>";
		for($j=0;$j<12;$j++){


				$m_hit=0;$zx=0;$good=-1;
				foreach(@TOWN_DATA){
					($zzname,$zzcon,$zznum,$zznou,$zzsyo,$zzshiro,$zznou_max,$zzsyo_max,$zzshiro_max,$zzpri,$zzx,$zzy,$zzsouba,$zzdef_att,$zzsub1,$zzsub2,$z[0],$z[1],$z[2],$z[3],$z[4],$z[5],$z[6],$z[7],$zzname1,$zzname2,$zzbong1,$zzbong2,$zzbong3)=split(/<>/);
					$good++;
	if($zzname2 eq "1"){
	$jiname ="����";
	}elsif($zzname2 eq "2"){
	$jiname ="����";
	}elsif($zzname2 eq "3"){
	$jiname ="���";
	}


					if("$zzx" eq "$j" && "$zzy" eq "$i"){$m_hit=1;last;}
					$zx++;
				}
				$col="";
				if($m_hit){
					if($zx eq $kpos && ($zzname eq "����" || $zzname eq "���" || $zzname eq "���" || $zzname eq "����" || $zzname eq "��" || $zzname eq "��â" || $zzname eq "�Ǿ�" || $zzname eq "��")){
						if($kcon eq $zzcon){
						print "<TH bgcolor=$ELE_BG[$cou_ele[$zzcon]]><form action=$COMMAND method=POST>$no_list<input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=mode value=$comlist><input type=hidden name=num value=$good><input type=image src=\"$IMG/bg31.gif\" alt='$zzname��$cou_name[$zzcon]��
���:$zznum
���:$zznou/$zznou_max
���:$zzsyo/$zzsyo_max
���:$zzsub1/1200
�ν�:$zzpri
����:$zzshiro/$zzshiro_max
���:$zzdef_att/1000
�ü�:$zzsouba
����:$jiname'>
</TH></form>";
						}else{
						print "<TH bgcolor=$ELE_BG[$cou_ele[$zzcon]]><img src=\"$IMG/bg31.gif\" alt='$zzname��$cou_name[$zzcon]��'></TH></form>";
						}
					}elsif($zx eq $kpos && ($zzname eq "����" || $zzname eq "õ��" || $zzname eq "����" || $zzname eq "����" || $zzname eq "����" || $zzname eq "����" || $zzname eq "���" || $zzname eq "����" || $zzname eq "����" || $zzname eq "�û�" || $zzname eq "��" || $zzname eq "�ܾ�" || $zzname eq "����" || $zzname eq "ȸ��" || $zzname eq "�����" || $zzname eq "���")){
						if($kcon eq $zzcon){
						print "<TH bgcolor=$ELE_BG[$cou_ele[$zzcon]]><form action=$COMMAND method=POST>$no_list<input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=mode value=$comlist><input type=hidden name=num value=$good><input type=image src=\"$IMG/bg11.gif\" alt='$zzname��$cou_name[$zzcon]��
���:$zznum
���:$zznou/$zznou_max
���:$zzsyo/$zzsyo_max
���:$zzsub1/1200
�ν�:$zzpri
����:$zzshiro/$zzshiro_max
���:$zzdef_att/1000
�ü�:$zzsouba
����:$jiname'>
</TH></form>";
						}else{
						print "<TH bgcolor=$ELE_BG[$cou_ele[$zzcon]]><img src=\"$IMG/bg11.gif\" alt='$zzname��$cou_name[$zzcon]��'></TH></form>";
						}
					}elsif($zx eq $kpos && ($zzname eq "ȫ��" || $zzname eq "��" || $zzname eq "����" || $zzname eq "����" || $zzname eq "����" || $zzname eq "����" || $zzname eq "��" || $zzname eq "����" || $zzname eq "����" || $zzname eq "�Ϻ�" || $zzname eq "����" || $zzname eq "��" || $zzname eq "����")){
						if($kcon eq $zzcon){
						print "<TH bgcolor=$ELE_BG[$cou_ele[$zzcon]]><form action=$COMMAND method=POST>$no_list<input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=mode value=$comlist><input type=hidden name=num value=$good><input type=image src=\"$IMG/bg21.gif\" alt='$zzname��$cou_name[$zzcon]��
���:$zznum
���:$zznou/$zznou_max
���:$zzsyo/$zzsyo_max
���:$zzsub1/1200
�ν�:$zzpri
����:$zzshiro/$zzshiro_max
���:$zzdef_att/1000
�ü�:$zzsouba
����:$jiname'>
</TH></form>";
						}else{
						print "<TH bgcolor=$ELE_BG[$cou_ele[$zzcon]]><img src=\"$IMG/bg21.gif\" alt='$zzname��$cou_name[$zzcon]��'></TH></form>";
						}
					}elsif($zx eq $kpos && ($zzname eq "����" || $zzname eq "�ǳ�" || $zzname eq "�" || $zzname eq "����" || $zzname eq "�˰�" || $zzname eq "�ڵ�" || $zzname eq "����" || $zzname eq "����" || $zzname eq "����" || $zzname eq "�ž�" || $zzname eq "���" || $zzname eq "���" || $zzname eq "����" || $zzname eq "����" || $zzname eq "����" || $zzname eq "�ż�")){
						if($kcon eq $zzcon){
						print "<TH bgcolor=$ELE_BG[$cou_ele[$zzcon]]><form action=$COMMAND method=POST>$no_list<input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=mode value=$comlist><input type=hidden name=num value=$good><input type=image src=\"$IMG/bg01.gif\" alt='$zzname��$cou_name[$zzcon]��
���:$zznum
���:$zznou/$zznou_max
���:$zzsyo/$zzsyo_max
���:$zzsub1/1200
�ν�:$zzpri
����:$zzshiro/$zzshiro_max
���:$zzdef_att/1000
�ü�:$zzsouba
����:$jiname'>
</TH></form>";
						}else{
						print "<TH bgcolor=$ELE_BG[$cou_ele[$zzcon]]><img src=\"$IMG/bg01.gif\" alt='$zzname��$cou_name[$zzcon]��'></TH></form>";
						}
					}elsif($zzname eq "����" || $zzname eq "���" || $zzname eq "���" || $zzname eq "����" || $zzname eq "��" || $zzname eq "��â" || $zzname eq "�Ǿ�" || $zzname eq "��"){
						if($kcon eq $zzcon){
						print "<TH bgcolor=$ELE_BG[$cou_ele[$zzcon]]><form action=$COMMAND method=POST>$no_list<input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=mode value=$comlist><input type=hidden name=num value=$good><input type=image src=\"$IMG/bg3.gif\" alt='$zzname��$cou_name[$zzcon]��
���:$zznum
���:$zznou/$zznou_max
���:$zzsyo/$zzsyo_max
���:$zzsub1/1200
�ν�:$zzpri
����:$zzshiro/$zzshiro_max
���:$zzdef_att/1000
�ü�:$zzsouba
����:$jiname'>
</TH></form>";
						}else{
						print "<TH bgcolor=$ELE_BG[$cou_ele[$zzcon]]><img src=\"$IMG/bg3.gif\" alt='$zzname��$cou_name[$zzcon]��'></TH></form>";
						}
					}elsif($zzname eq "ȫ��" || $zzname eq "��" || $zzname eq "����" || $zzname eq "����" || $zzname eq "����" || $zzname eq "����" || $zzname eq "��" || $zzname eq "����" || $zzname eq "����" || $zzname eq "�Ϻ�" || $zzname eq "����" || $zzname eq "��" || $zzname eq "����"){
						if($kcon eq $zzcon){
						print "<TH bgcolor=$ELE_BG[$cou_ele[$zzcon]]><form action=$COMMAND method=POST>$no_list<input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=mode value=$comlist><input type=hidden name=num value=$good><input type=image src=\"$IMG/bg2.gif\" alt='$zzname��$cou_name[$zzcon]��
���:$zznum
���:$zznou/$zznou_max
���:$zzsyo/$zzsyo_max
���:$zzsub1/1200
�ν�:$zzpri
����:$zzshiro/$zzshiro_max
���:$zzdef_att/1000
�ü�:$zzsouba
����:$jiname'>
</TH></form>";
						}else{
						print "<TH bgcolor=$ELE_BG[$cou_ele[$zzcon]]><img src=\"$IMG/bg2.gif\" alt='$zzname��$cou_name[$zzcon]��'></TH></form>";
						}
					}elsif($zzname eq "����" || $zzname eq "õ��" || $zzname eq "����" || $zzname eq "����" || $zzname eq "����" || $zzname eq "����" || $zzname eq "���" || $zzname eq "����" || $zzname eq "����" || $zzname eq "�û�" || $zzname eq "��" || $zzname eq "�ܾ�" || $zzname eq "����" || $zzname eq "ȸ��" || $zzname eq "�����" || $zzname eq "���"){
						if($kcon eq $zzcon){
						print "<TH bgcolor=$ELE_BG[$cou_ele[$zzcon]]><form action=$COMMAND method=POST>$no_list<input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=mode value=$comlist><input type=hidden name=num value=$good><input type=image src=\"$IMG/bg1.gif\" alt='$zzname��$cou_name[$zzcon]��
���:$zznum
���:$zznou/$zznou_max
���:$zzsyo/$zzsyo_max
���:$zzsub1/1200
�ν�:$zzpri
����:$zzshiro/$zzshiro_max
���:$zzdef_att/1000
�ü�:$zzsouba
����:$jiname'>
</TH></form>";
						}else{
						print "<TH bgcolor=$ELE_BG[$cou_ele[$zzcon]]><img src=\"$IMG/bg1.gif\" alt='$zzname��$cou_name[$zzcon]��'></TH></form>";
						}
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
						if($kcon eq $zzcon){
						print "<TH bgcolor=$ELE_BG[$cou_ele[$zzcon]]><form action=$COMMAND method=POST>$no_list<input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=mode value=$comlist><input type=hidden name=num value=$good><input type=image src=\"$IMG/bg0.gif\" alt='$zzname��$cou_name[$zzcon]��
���:$zznum
���:$zznou/$zznou_max
���:$zzsyo/$zzsyo_max
���:$zzsub1/1200
�ν�:$zzpri
����:$zzshiro/$zzshiro_max
���:$zzdef_att/1000
�ü�:$zzsouba
����:$jiname'>
</TH></form>";
						}else{
						print "<TH bgcolor=$ELE_BG[$cou_ele[$zzcon]]><img src=\"$IMG/bg0.gif\" alt='$zzname��$cou_name[$zzcon]��'></TH></form>";
						}
					}
				}else{
					print "<TH> </TH>";
				}
		}
		print "</TR>";
	}






print <<"EOM";
        </TBODY>
                                                            </tr>
      </TABLE>
<br><br>
<b>�߷��ϰ��� �ϴ� �ڱ� ���� ���������� Ŭ�����ּ���.</b>
<br>
<center>
<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="���ƿ´�"></form>
</TD></TR></TABLE>
                    </td>
                    <td width="8" height="467" rowspan="6">
                    </td>
                </tr>
                <tr>
                    <td width="70" height="82">
                        <p align="center"><img src="$IMG/$kchara.gif" width="64" height="80" border="0"></p>
                    </td>
                </tr>
                <tr>
                    <td width="70" height="37">
                        <p align="center"><font color="white" face="����"><span style="font-size:9pt;">$kname</span></font></p>
                    </td>
                </tr>
                <tr>
                    <td width="70" height="83">
                    </td>
                </tr>
                <tr>
                    <td width="312" height="35" colspan="5">
                    </td>
                </tr>
                <tr>
                    <td width="288" height="196" colspan="4" valign="up">
<font color="white" face="����"><span style="font-size:9pt;">�ڽ��� �Ҽӵ� �δ���� �ٸ� ���÷� �̵��մϴ�.<br>�ڱ� ���� ���� �ڽ��� �δ���� �̵���ų ���� �ֽ��ϴ�.</span></font></td>
                    <td width="24" height="196">
                    </td>
                </tr>
            </table>
        </td>
    </tr>
</table>
        </td>
    </tr>
    <tr>
        <td>
            <img src="$IMG/down.gif">
        </td>
    </tr>
</table>
</body>
EOM

	&FOOTER;

	exit;

}





sub BAL12 {

	if($in{'no'} eq ""){&ERR("NO:�� �Էµ��� �ʾҽ��ϴ�.");}
	&CHARA_MAIN_OPEN;
	&CHARA_ITEM_OPEN;
	&TOWN_DATA_OPEN("$kpos");
	&COUNTRY_DATA_OPEN($kcon);
	&TIME_DATA;
	foreach(@no){
		$no_list .= "<input type=hidden name=no value=$_>"
	}

	$comlist = 20;

	&HEADER;
	$no = $in{'no'} + 1;
	open(IN,"$UNIT_LIST") or &ERR("������ ������ ������ �ʽ��ϴ�.");
	@UNI_DATA = <IN>;
	close(IN);

	@UNI_DATA2 = @UNI_DATA;



	print <<"EOM";
<STYLE>BODY {
	CURSOR: url('samnet.cur')
}
A {
	CURSOR: url('samnet.ani'); TEXT-DECORATION: none
}
</STYLE>
<BODY oncontextmenu="return false" onselectstart="return false" ondragstart="return false">
<body leftmargin="0" marginwidth="0" topmargin="0" marginheight="0">
<table align="center" width="950">
    <tr>
        <td>
            <img src="$IMG/up.gif">
        </td>
    </tr>
    <tr height="600">
        <td background="$IMG/backg.gif">
<table align="center" border="1" cellspacing="0" width="752" height="492" bordercolordark="white" bordercolorlight="black">
    <tr>
        <td width="1101" height="492" background="$IMG/cola.jpg">
            <table cellpadding="0" cellspacing="0" width="752" height="488" bordercolordark="white" bordercolorlight="black">
                <tr>
                    <td width="752" height="22" colspan="8">
                        <p>&nbsp;</p>
                    </td>
                </tr>
                <tr>
                    <td width="11" height="467" rowspan="6">
                        <p>&nbsp;</p>
                    </td>
                    <td width="52" height="236" rowspan="4">
                        <p>&nbsp;</p>
                    </td>
                    <td width="141" height="236" rowspan="4">
                        <table cellpadding="0" cellspacing="0">
                            <tr>
                                <td width="131" height="18">
                                    <p><font color="white"><span style="font-size:9pt;">$cou_name[$kcon]��</span></font></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="131" height="18">
				<table cellpadding="0" cellspacing="0"><tr><td width="$kstr1" bgcolor="#006600"><font color="white"><span style="font-size:8pt;">$kstrt</span></font></td></tr></table>
                                </td>
                            </tr>
                            <tr>
                                <td width="131" height="18">
				<table cellpadding="0" cellspacing="0"><tr><td width="$kint1" bgcolor="#006600"><font color="white"><span style="font-size:8pt;">$kintt</span></font></td></tr></table>
                                </td>
                            </tr>
                            <tr>
                                <td width="131" height="18">
				<table cellpadding="0" cellspacing="0"><tr><td width="$klea1" bgcolor="#006600"><font color="white"><span style="font-size:8pt;">$kleat</span></font></td></tr></table>
                                </td>
                            </tr>
                            <tr>
                                <td width="131" height="18">
                                <table cellpadding="0" cellspacing="0"><tr><td width="$kcha1" bgcolor="#006600"><font color="white"><span style="font-size:8pt;">$kchat</span></font></td></tr></table>
                                </td>
                            </tr>
                            <tr>
                                <td width="131" height="18">
                                <table cellpadding="0" cellspacing="0"><tr><td width="$kgold1" bgcolor="#006600"><font color="white"><span style="font-size:8pt;">$kgold</span></font></td></tr></table>
                                </td>
                            </tr>
                            <tr>
                                <td width="131" height="18">
                                <table cellpadding="0" cellspacing="0"><tr><td width="$krice1" bgcolor="#006600"><font color="white"><span style="font-size:8pt;">$krice</span></font></td></tr></table>
                                </td>
                            </tr>
                            <tr>
                                <td width="131" height="18">
                                <table cellpadding="0" cellspacing="0"><tr><td width="$kcex1" bgcolor="#006600"><font color="white"><span style="font-size:8pt;">$kcex</span></font></td></tr></table>
                                </td>
                            </tr>
                            <tr>
                                <td width="131" height="18">
                                <table cellpadding="0" cellspacing="0"><tr><td width="$ksol1" bgcolor="#006600"><font color="white"><span style="font-size:8pt;">$ksol</span></font></td></tr></table>
                                </td>
                            </tr>
                            <tr>
                                <td width="131" height="18">
                                <table cellpadding="0" cellspacing="0"><tr><td width="$kgat" bgcolor="#006600"><font color="white"><span style="font-size:8pt;">$kgat</span></font></td></tr></table>
                                </td>
                            </tr>
                        </table>

                    </td>
                    <td width="25" height="236" rowspan="4">
                    </td>
                    <td width="70" height="34">
                    </td>
                    <td width="24" height="236" rowspan="4">
&nbsp;                  </td>
                    <td width="421" height="467" rowspan="6">
<TABLE border=0 width=100% height=80%><TR><TD>
<center>

</span></font>
<p>[�̵��� �δ���� ����]<BR>
<form action="$COMMAND" method="POST"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<select name=num1>
EOM


		foreach(@UNI_DATA){
		($unit_id,$uunit_name,$ucon,$ureader,$uid,$uname,$uchara,$umes,$uflg)=split(/<>/);
if("$ucon" eq "$kcon" && $ureader){

			$unit_num=1;
			$unit_list = "$uname";

		if($uid eq $kid){
				foreach(@UNI_DATA2){
					($unit_id2,$uunit_name2,$ucon2,$ureader2,$uid2,$uname2,$uchara2,$umes2,$uflg2)=split(/<>/);
					if("$unit_id" eq "$unit_id2" && !$ureader2){
						$unit_list .= ",$uname2";
						$unit_num++;
						$u_member .= "<option value=$uname2>$uname2";
						}
				}

			}else{
				foreach(@UNI_DATA2){
					($unit_id2,$uunit_name2,$ucon2,$ureader2,$uid2,$uname2,$uchara2,$umes2,$uflg2)=split(/<>/);
					if("$unit_id" eq "$unit_id2" && !$ureader2){
						$unit_list .= ",$uname2";
						$unit_num++;
										}
							}
			}
}
}
print <<"EOM";
$u_member
</select>
<center>
<input type=hidden name=no value=$in{'no'}>
<input type=hidden name=num value=$in{'num'}>
<input type=hidden name=mode value=54>
<input type=submit value="�߷��Ѵ�"></form>
<br>
<center>
<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="���ƿ´�"></form>
</TD></TR></TABLE>
                    </td>
                    <td width="8" height="467" rowspan="6">
                    </td>
                </tr>
                <tr>
                    <td width="70" height="82">
                        <p align="center"><img src="$IMG/$kchara.gif" width="64" height="80" border="0"></p>
                    </td>
                </tr>
                <tr>
                    <td width="70" height="37">
                        <p align="center"><font color="white" face="����"><span style="font-size:9pt;">$kname</span></font></p>
                    </td>
                </tr>
                <tr>
                    <td width="70" height="83">
                    </td>
                </tr>
                <tr>
                    <td width="312" height="35" colspan="5">
                    </td>
                </tr>
                <tr>
                    <td width="288" height="196" colspan="4" valign="up">
<font color="white" face="����"><span style="font-size:9pt;">�ڽ��� �Ҽӵ� �δ���� �ٸ� ���÷� �̵��մϴ�.<br>�ڱ� ���� ���� �ڽ��� �δ���� �̵���ų ���� �ֽ��ϴ�.</span></font></td>
                    <td width="24" height="196">
                    </td>
                </tr>
            </table>
        </td>
    </tr>
</table>
        </td>
    </tr>
    <tr>
        <td>
            <img src="$IMG/down.gif">
        </td>
    </tr>
</table>
</body>
EOM

	&FOOTER;

	exit;

}




sub BAL2 {
	if($in{'no'} eq ""){&ERR("NO:�� �Էµ��� �ʾҽ��ϴ�.");}

	&CHARA_MAIN_OPEN;
	&TOWN_DATA_OPEN("$kpos");
	&TIME_DATA;

	$num = $in{'num'};
	$hit=0;
	foreach(@z){
		if($_ eq $num){
			$hit=1;
		}
	}

	open(IN,"./charalog/command/$kid.cgi");
	@COM_DATA = <IN>;
	close(IN);

	$mes_num = @COM_DATA;

	if($mes_num > $MAX_COM) { pop(@COM_DATA); }

	@NEW_COM_DATA=();$i=0;
	if($in{'no'} eq "all"){
		while(@NEW_COM_DATA < $MAX_COM){
				push(@NEW_COM_DATA,"$in{'mode'}<><>$in{'num1'}�� $town_name[$num]������ �߷�<>$tt<>$in{'num1'}<>$in{'num'}<><>\n");
		}
		$no = $in{'no'};
	}else{
		foreach(@COM_DATA){
			($cid,$cno,$cname,$ctime,$csub,$cnum,$cend) = split(/<>/);
			$ahit=0;
			foreach(@no){
				if($i eq $_){
					$ahit=1;
					push(@NEW_COM_DATA,"$in{'mode'}<><>$in{'num1'}�� $town_name[$num]������ �߷�<>$tt<>$in{'num1'}<>$in{'num'}<><>\n");
					$lno = $_ + 1;
					$no .= "$lno,";
				}
			}
			if(!$ahit){
				push(@NEW_COM_DATA,"$_");
			}

			$i++;
		}
	}

	open(OUT,">./charalog/command/$kid.cgi") or &ERR('������ ���� �ʾҽ��ϴ�.');
	print OUT @NEW_COM_DATA;
	close(OUT);

	&HEADER;

	print <<"EOM";
<CENTER><hr size=0><h2>NO:$no�� $town_name[$num]�� �̵��� �Է��߽��ϴ�.</h2><p>
<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="Ȯ��"></form></CENTER>
EOM

	&FOOTER;

	exit;

}
1;