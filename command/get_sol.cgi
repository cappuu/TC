sub GET_SOL {

	if($in{'no'} eq ""){&ERR("NO:�� �Էµ��� �ʾҽ��ϴ�.");}
	&CHARA_MAIN_OPEN;
	&CHARA_ITEM_OPEN;
	&TOWN_DATA_OPEN($kpos);
	&TIME_DATA;
	&COUNTRY_DATA_OPEN("$kcon");

	&HEADER;
	$no = $in{'no'} + 1;

	$get_sol = ($kleat*30) - $ksol;

	foreach(@TOWN_DATA){
	($zzname,$zzcon,$zznum,$zznou,$zzsyo,$zzshiro,$zznou_max,$zzsyo_max,$zzshiro_max,$zzpri,$zzx,$zzy)=split(/<>/);
	if("$zzx" eq "$j" && "$zzy" eq "$i"){$m_hit=1;last;}
	$zx++;
				}


	if($kskill =~ /Fc/){
		$max0 = $SOL_PRICE[0] * 2;
		$max1 = $SOL_PRICE[1] * 2;
		$max2 = $SOL_PRICE[2] * 2;
		$max3 = $SOL_PRICE[3] * 2;
		$max4 = $SOL_PRICE[4] * 2;
		$max5 = $SOL_PRICE[5] * 2;
		$max6 = $SOL_PRICE[6] * 2;
		$max7 = $SOL_PRICE[7] * 2;
		$max8 = $SOL_PRICE[8] * 2;
		$max9 = $SOL_PRICE[9] * 2;
		$max10 = $SOL_PRICE[10] * 2;
		$max11 = $SOL_PRICE[11] * 2;
		$max12 = $SOL_PRICE[12] * 2;
		$max13 = $SOL_PRICE[13] * 2;
		$max14 = $SOL_PRICE[14] * 2;
		$max15 = $SOL_PRICE[15] * 2;
		$max16 = $SOL_PRICE[16] * 2;
		$max17 = $SOL_PRICE[17] * 2;
		$max18 = $SOL_PRICE[18] * 2;
		$max19 = $SOL_PRICE[19] * 2;
		$max20 = $SOL_PRICE[20] * 2;
	}else{
		$max0 = $SOL_PRICE[0];
		$max1 = $SOL_PRICE[1];
		$max2 = $SOL_PRICE[2];
		$max3 = $SOL_PRICE[3];
		$max4 = $SOL_PRICE[4];
		$max5 = $SOL_PRICE[5];
		$max6 = $SOL_PRICE[6];
		$max7 = $SOL_PRICE[7];
		$max8 = $SOL_PRICE[8];
		$max9 = $SOL_PRICE[9];
		$max10 = $SOL_PRICE[10];
		$max11 = $SOL_PRICE[11];
		$max12 = $SOL_PRICE[12];
		$max13 = $SOL_PRICE[13];
		$max14 = $SOL_PRICE[14];
		$max15 = $SOL_PRICE[15];
		$max16 = $SOL_PRICE[16];
		$max17 = $SOL_PRICE[17];
		$max18 = $SOL_PRICE[18];
		$max19 = $SOL_PRICE[19];
		$max20 = $SOL_PRICE[20];
	}

	foreach(@no){
		$no_list .= "<input type=hidden name=no value=$_>"
	}

		if($zsub1 > 100){
		$by1 = "FFFFFF"}else{$by1 = "FF0000"}
		if($zsub1 > 250){
		$by2 = "FFFFFF"}else{$by2 = "FF0000"}
		if($zsub1 > 450){
		$by3 = "FFFFFF"}else{$by3 = "FF0000"}
		if(($zname eq "����" || $zname eq "����" || $zname eq "�˰�" || $zname eq "�ڵ�" || $zname eq "�ǳ�" || $zname eq "�" || $zname eq "����" || $zname eq "����" || $zname eq "����" || $zname eq "�ž�" || $zname eq "���" || $zname eq "���" || $zname eq "����" || $zname eq "����" || $zname eq "����" || $zname eq "�ż�") && $zsub1 > 500){
		$by4 = "FFFFFF"}else{$by4 = "FF0000"}
		if($zsub1 > 750){
		$by5 = "FFFFFF"}else{$by5 = "FF0000"}
		if($zsub1 > 800){
		$by6 = "FFFFFF"}else{$by6 = "FF0000"}
		if($zsub1 > 1000){
		$by7 = "FFFFFF"}else{$by7 = "FF0000"}
		if(($zname eq "����" || $zname eq "���" || $zname eq "����" || $zname eq "��â" || $zname eq "���" || $zname eq "��" || $zname eq "�Ǿ�" || $zname eq "��") && $zsub1 > 1150){
		$by8 = "FFFFFF"}else{$by8 = "FF0000"}
		if($zname eq "�" && $zsub1 > 750){
		$by9 = "FFFFFF"}else{$by9 = "FF0000"}
		if(($zname eq "����" || $zname eq "����" || $zname eq "��" || $zname eq "����" || $zname eq "����" || $zname eq "����" || $zname eq "����" || $zname eq "����" || $zname eq "����" || $zname eq "�˰�" || $zname eq "�ڵ�" || $zname eq "����" || $zname eq "����" || $zname eq "�ǳ�" || $zname eq "����" || $zname eq "�����" || $zname eq "����") && $zsub1 > 1150){
		$by10 = "FFFFFF"}else{$by10 = "FF0000"}
		if(($zname eq "����" || $zname eq "����" || $zname eq "��" || $zname eq "����" || $zname eq "����" || $zname eq "����") && $zsub1 > 1100){
		$by11 = "FFFFFF"}else{$by11 = "FF0000"}
		if($zname eq "�����" && $zsub1 > 1100){
		$by12 = "FFFFFF"}else{$by12 = "FF0000"}
		if($zsub1 > 1199){
		$by13 = "FFFFFF"}else{$by13 = "FF0000"}
		if($zsub1 > 900){
		$by14 = "FFFFFF"}else{$by14 = "FF0000"}
		if($zname eq "ȸ��" && $zsub1 > 899){
		$by15 = "FFFFFF"}else{$by15 = "FF0000"}
		if($zsub1 > 1199){
		$by16 = "FFFFFF"}else{$by16 = "FF0000"}
		if($zsub1 > 999){
		$by17 = "FFFFFF"}else{$by17 = "FF0000"}
		if($zsub1 > 749){
		$by18 = "FFFFFF"}else{$by18 = "FF0000"}
		if($zsub1 > 1099){
		$by19 = "FFFFFF"}else{$by19 = "FF0000"}


	print <<"EOM";
<STYLE>BODY {
	CURSOR: url('samnet.cur')
}
A {
	CURSOR: url('samnet.ani'); TEXT-DECORATION: none
}
</STYLE>
<body bgcolor="white" text="white" link="blue" vlink="purple" alink="red" leftmargin="0" marginwidth="0" topmargin="0" marginheight="0">
<table align="center" cellpadding="0" cellspacing="0" width="937">
    <tr>
        <td width="937">
            <p><img src="$IMG/up.gif" width="950" height="93" border="0"></p>
        </td>
    </tr>
    <tr>
        <td width="937" height="215" background="$IMG/backg.gif">
&nbsp;
            <table align="center" cellpadding="0" cellspacing="0" width="677">
                <tr>
                    <td width="677">
                        <p><img src="$IMG/law1.gif" width="700" height="22" border="0"></p>
                    </td>
                </tr>
                <tr>
                    <td width="677" height="216" background="$IMG/law3.gif">
<center><TABLE bgcolor=$ELE_BG[$xele]><TBODY bgcolor=$ELE_C[$xele]>
<TR><TH colspan=7 bgcolor=$ELE_BG[$xele]><font color=$ELE_C[$xele]>$kname</font></TH></TR>
<TR><TD rowspan=2 width=5><img src=$IMG/$kchara.gif></TD><TD>����</TD><TH>$kstrt</TH><TD>����</TD><TH>$kintt</TH><TD>��ַ�</TD><TH>$kleat</TH></TR>
<TR><TD>��</TD><TH>$kgold</TH><TD>��</TD><TH>$krice</TH><TD>����</TD><TH>$kcex</TH></TR>
<TR><TD>������ġ</TD><TH colspan=2>$zname��</TH><TD>����</TD><TH>$ksol</TH><TD>�Ʒ�</TD><TH>$kgat</TH></TR>
</TBODY></TABLE><br>

<table align="center" cellpadding="0" cellspacing="0" width="435" height="200" background="$IMG/get_sol.jpg">
    <tr>
        <td>
            <div align="right">
                <table cellpadding="0" cellspacing="0" width="328" height="200" bordercolordark="black" bordercolorlight="black">
                    <tr>
                        <td width="328" height="76" colspan="5">
                        </td>
                    </tr>
                    <tr>
                        <td width="80" valign="up">
                            <p align="center"><span style="font-size:9pt;"><a href="http://chilrang.cafe24.com/sam/command.cgi#1">����</a><br><a href="http://chilrang.cafe24.com/sam/command.cgi#2">�ú�</a><br><a href="http://chilrang.cafe24.com/sam/command.cgi#4">���庸��</a><br><a href="http://chilrang.cafe24.com/sam/command.cgi#11">��Ǻ�</a><br><a href="http://chilrang.cafe24.com/sam/command.cgi#15">Ȳ����</a><br><a href="http://chilrang.cafe24.com/sam/command.cgi#19">����</a><br><a href="http://chilrang.cafe24.com/sam/command.cgi#20">����</a></span></p>
                        </td>
                        <td width="80" valign="up">
                            <p align="center"><span style="font-size:9pt;"><a href="http://chilrang.cafe24.com/sam/command.cgi#6">�⺴</a><br><a href="http://chilrang.cafe24.com/sam/command.cgi#10">�ڳ�����</a><br><a href="http://chilrang.cafe24.com/sam/command.cgi#12">ö�⺴</a><br><a href="http://chilrang.cafe24.com/sam/command.cgi#13">ȭ��</a></span></p>
                        </td>
                        <td width="81" valign="up">
                            <p align="center"><span style="font-size:9pt;"><a href="http://chilrang.cafe24.com/sam/command.cgi#3">â��</a><br><a href="http://chilrang.cafe24.com/sam/command.cgi#5">��κ�</a><br><a href="http://chilrang.cafe24.com/sam/command.cgi#7">�Ǻ�</a><br><a href="http://chilrang.cafe24.com/sam/command.cgi#16">�����</a><br><a href="http://chilrang.cafe24.com/sam/command.cgi#18">�غ�</a></span></p>
                        </td>
                        <td width="79" valign="up">
                            <p align="center"><span style="font-size:9pt;"><a href="http://chilrang.cafe24.com/sam/command.cgi#8">�űͺ�</a><br><a href="http://chilrang.cafe24.com/sam/command.cgi#9">Ȳ�Ǳ�����</a><br><a href="http://chilrang.cafe24.com/sam/command.cgi#14">�߼���</a><br><a href="http://chilrang.cafe24.com/sam/command.cgi#17">�ļ���</a></span></p>
                        </td>
                        <td width="8" valign="up">
                        </td>
                    </tr>
                </table>
            </div>
        </td>
    </tr>
</table>

<br>
                        <table align="center" border="1" cellspacing="0" width="438" bordercolordark="white" bordercolorlight="black">
                            <tr>
                                <td width="432" height="35" colspan="2" bgcolor="black">
                                    <p align="center"><span style="font-size:10pt;"><b><a name="1"></a>����</b></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">����</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">�����迭</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">���ݷ�</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">��(0)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">�����</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">��(0)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">�����ݷ�</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">��(0)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">������</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="blue">���� 
                                    100% ���� 100% ��� 100%</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">����(30���)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">$max0</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p><span style="font-size:9pt;">����� �ҼҸ�(60���)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">10</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="65" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">����</span></p>
                                </td>
                                <td width="300" height="65" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">������ 
                                    ������� �⺻���� Ŭ�����Դϴ�. �� ���ݿ� 
                                    ���ݷ� �����, �����ݷ¸����� ������ ���¿� 
                                    �ڽ��� �ְ� ��뺴���� ���ٸ�&nbsp;�Ẽ���� 
                                    �����Դϴ�.</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="432" height="22" colspan="2" bgcolor="black">
<form action="$COMMAND" method="POST">
<p align="right"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<input type=text name=num value=$get_sol size=4>���� 
$no_list<input type=hidden name=type value=0><input type=hidden name=mode value=10><input type=submit value="����Ѵ�">
</form>
                                </td>
                            </tr>
                        </table><br>
                        <table align="center" border="1" cellspacing="0" width="438" bordercolordark="white" bordercolorlight="black">
                            <tr>
                                <td width="432" height="35" colspan="2" bgcolor="black">
                                    <p align="center"><font color="$by1"><span style="font-size:10pt;"><b><a name="2"></a>�ú�</b></span></font></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">����</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">�����迭</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">���ݷ�</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">�ڡ�(30)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">�����</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">��(0)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">�����ݷ�</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">�ڡ�(30)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">������</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="blue">���� 
                                    95% ���� 100% </font><font color="#00CC00">��� 115%</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">����(30���)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">$max1</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p><span style="font-size:9pt;">����� �ҼҸ�(60���)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">10</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="65" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">����</span></p>
                                </td>
                                <td width="300" height="65" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">�������� 
                                    �ణ�� ���� �����Դϴ�. ������ �������� 
                                    �ٸ� ���� ���� ������ �����ݷ��� ���� ���Դϴ�.</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="432" height="22" colspan="2" bgcolor="black">
<form action="$COMMAND" method="POST">
                                        <p align="right"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<input type=text name=num value=$get_sol size=4>���� 
$no_list<input type=hidden name=type value=1><input type=hidden name=mode value=10><input type=submit value="����Ѵ�">
</form>
                                </td>
                            </tr>
                        </table><br>
                        <table align="center" border="1" cellspacing="0" width="438" bordercolordark="white" bordercolorlight="black">
                            <tr>
                                <td width="432" height="35" colspan="2" bgcolor="black">
                                    <p align="center"><font color="$by2"><span style="font-size:10pt;"><b><a name="3"></a>â��</b></span></font></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">����</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">â���迭</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">���ݷ�</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">��(15)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">�����</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">�ڡڡ�(45)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">�����ݷ�</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">��(10)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">������</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="#CC3300">���� 
                                    90%</font><font color="blue"> ���� 100% </font><font color="#00CC00">��� 120%</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">����(30���)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">$max2</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p><span style="font-size:9pt;">����� �ҼҸ�(60���)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">20</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="65" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">����</span></p>
                                </td>
                                <td width="300" height="65" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">â���� 
                                    �Ѱ��ݿ� �����Ҹ��� ������� ���߰� �ֽ��ϴ�. 
                                    �Դٰ� ��ǿ��� Ưȭ�Ǿ� ��ǿ��� ���� 
                                    �ҽ� Ưȭ�� ������� ������ �ֽ��ϴ�.</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="432" height="22" colspan="2" bgcolor="black">
<form action="$COMMAND" method="POST">
                                        <p align="right"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<input type=text name=num value=$get_sol size=4>���� 
$no_list<input type=hidden name=type value=2><input type=hidden name=mode value=10><input type=submit value="����Ѵ�">
</form>
                                </td>
                            </tr>
                        </table><br>
                        <table align="center" border="1" cellspacing="0" width="438" bordercolordark="white" bordercolorlight="black">
                            <tr>
                                <td width="432" height="35" colspan="2" bgcolor="black">
                                    <p align="center"><font color="$by3"><span style="font-size:10pt;"><b><a name="4"></a>���庸��</b></span></font></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">����</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">�����迭</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">���ݷ�</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">�ڡ�(30)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">�����</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">�ڡ�(30)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">�����ݷ�</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">�ڡ�(30)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">������</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="blue">���� 
                                    100% </font><font color="#00CC00">���� 120%</font><font color="blue"> ��� 100%</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">����(30���)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">$max3</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">����� �ҼҸ�(60���)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">20</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="65" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">����</span></p>
                                </td>
                                <td width="300" height="65" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">���庸���� 
                                    ��õ�������Դϴ�. �Դٰ� �����󼺵� ���� 
                                    �������� ������ ���� ��𼭵��� ����ϱ� 
                                    ���� �����Դϴ�. ������ ��� �ѱ��� �پ 
                                    ������ ��� �ָ��� �����Դϴ�.</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="432" height="22" colspan="2" bgcolor="black">
<form action="$COMMAND" method="POST">
                                        <p align="right"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<input type=text name=num value=$get_sol size=4>���� 
$no_list<input type=hidden name=type value=3><input type=hidden name=mode value=10><input type=submit value="����Ѵ�">
</form>
                                </td>
                            </tr>
                        </table><br>
                        <table align="center" border="1" cellspacing="0" width="438" bordercolordark="white" bordercolorlight="black">
                            <tr>
                                <td width="432" height="35" colspan="2" bgcolor="black">
                                    <p align="center"><font color="$by4"><span style="font-size:10pt;"><b><a name="5"></a>��κ�</b></span></font></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">â���迭</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">â���迭</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">���ݷ�</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">��(0)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">�����</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">�ν��� 
                                    ����¿� ����</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">�����ݷ�</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">��(0)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">������</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="blue">���� 
                                    100% </font><font color="#CC3300">���� 90%</font><font color="blue"> ��� 100%</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">����(30���)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">$max16</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p><span style="font-size:9pt;">����� �ҼҸ�(60���)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">20</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="65" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">����</span></p>
                                </td>
                                <td width="300" height="65" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">��κ��� 
                                    �ڱ��� �����ϱ� �Ҹ��� �� �����ϰ� ���� 
                                    �� �ִ� �����Դϴ�. ����¿� ���� �ν��� 
                                    ����Ǳ� ������ �ش������� �νɸ� ���ٸ� 
                                    ȿ�������� ���Ƴ� �� �ֽ��ϴ�.</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="432" height="22" colspan="2" bgcolor="black">
<form action="$COMMAND" method="POST">
                                        <p align="right"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<input type=text name=num value=$get_sol size=4>���� 
$no_list<input type=hidden name=type value=16><input type=hidden name=mode value=10><input type=submit value="����Ѵ�">
</form>
                                </td>
                            </tr>
                        </table><br>
                        <table align="center" border="1" cellspacing="0" width="438" bordercolordark="white" bordercolorlight="black">
                            <tr>
                                <td width="432" height="35" colspan="2" bgcolor="black">
                                    <p align="center"><font color="$by5"><span style="font-size:10pt;"><b><a name="6"></a>�⺴</b></span></font></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">����</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">�⺴�迭</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">���ݷ�</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">�ڡڡڡ�(60)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">�����</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">��(15)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">�����ݷ�</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">��(0)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">������</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="#00CC00">���� 
                                    130%</font><font color="blue"> </font><font color="#CC3300">���� 90% ��� 70%</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">����(30���)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">$max4</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p><span style="font-size:9pt;">����� �ҼҸ�(60���)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">30</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="65" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">����</span></p>
                                </td>
                                <td width="300" height="65" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">�⺴�� 
                                    ���ݿ� Ưȭ�Ǿ����ϴ�. Ư�� ������ ������� 
                                    ������ ���� �����մϴ�. ������ ����� ������ 
                                    ����� ����� ���Դϴ�.</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="432" height="22" colspan="2" bgcolor="black">
<form action="$COMMAND" method="POST">
                                        <p align="right"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<input type=text name=num value=$get_sol size=4>���� 
$no_list<input type=hidden name=type value=4><input type=hidden name=mode value=10><input type=submit value="����Ѵ�">
</form>
                                </td>
                            </tr>
                        </table><br>
                        <table align="center" border="1" cellspacing="0" width="438" bordercolordark="white" bordercolorlight="black">
                            <tr>
                                <td width="432" height="35" colspan="2" bgcolor="black">
                                    <p align="center"><font color="$by6"><span style="font-size:10pt;"><b><a name="7"></a>�Ǻ�</b></span></font></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">����</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">â���迭</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">���ݷ�</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">�ڡ�(20)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">�����</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">����� 
                                    ����</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">�����ݷ�</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">�ڡڡ�(45)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">������</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="#CC3300">���� 
                                    80%</font><font color="blue"> </font><font color="#00CC00">���� 110%</font><font color="blue"> ��� 100%</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">����(30���)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">$max6</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p><span style="font-size:9pt;">����� �ҼҸ�(60���)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">40</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="65" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">����</span></p>
                                </td>
                                <td width="300" height="65" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">�Ǻ��� 
                                    �η��� �����Դϴ�. ���� ����� ����Ǳ� 
                                    ������ ����� ���� ������ ���� ���°� 
                                    ���Ҿ� ���� ������ �볳���� �ʱ� �����Դϴ�. 
                                    ���ݷ°� �����ݷµ� �߱��̾ �������� 
                                    ��ȯ�ص� ������ �����Դϴ�.</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="432" height="22" colspan="2" bgcolor="black">
<form action="$COMMAND" method="POST">
                                        <p align="right"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<input type=text name=num value=$get_sol size=4>���� 
$no_list<input type=hidden name=type value=6><input type=hidden name=mode value=10><input type=submit value="����Ѵ�">
</form>
                                </td>
                            </tr>
                        </table><br>
                        <table align="center" border="1" cellspacing="0" width="438" bordercolordark="white" bordercolorlight="black">
                            <tr>
                                <td width="432" height="35" colspan="2" bgcolor="black">
                                    <p align="center"><font color="$by7"><span style="font-size:10pt;"><b><a name="8"></a>�űͺ�</b></span></font></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">����</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">�ͺ��迭</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">���ݷ�</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">������ 
                                    ����</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">�����</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">��(15)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">�����ݷ�</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">����/2 
                                    ����</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">������</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="blue">���� 
                                    100% </font><font color="#00CC00">���� 110%</font><font color="blue"> </font><font color="#CC3300">��� 90%</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">����(30���)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">$max5</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p><span style="font-size:9pt;">����� �ҼҸ�(60���)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">40</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="65" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">����</span></p>
                                </td>
                                <td width="300" height="65" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">������ 
                                    ���� Ưȭ �����Դϴ�. ���ݷ¿� ������ ����Ǿ� 
                                    ��� ������ ���� �����̾ ����� ������ 
                                    ���� ������ �� �ֽ��ϴ�. ������ ������ 
                                    ��μ� �������� ���������� ��ƽ��ϴ�. ��ų 
                                    ������͸����� ����� �� �ְ� ������ ���� ���� �� �ֽ��ϴ�.</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="432" height="22" colspan="2" bgcolor="black">
<form action="$COMMAND" method="POST">
                                        <p align="right"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<input type=text name=num value=$get_sol size=4>���� 
$no_list<input type=hidden name=type value=5><input type=hidden name=mode value=10><input type=submit value="����Ѵ�">
</form>
                                </td>
                            </tr>
                        </table><br>
                        <table align="center" border="1" cellspacing="0" width="438" bordercolordark="white" bordercolorlight="black">
                            <tr>
                                <td width="432" height="35" colspan="2" bgcolor="black">
                                    <p align="center"><font color="$by8"><span style="font-size:10pt;"><b><a name="9"></a>Ȳ�Ǳ�����</b></span></font></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">����</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">�ͺ��迭</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">���ݷ�</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">����+�ŷ� 
                                    ����</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">�����</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">����+�ŷ� 
                                    ����</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">�����ݷ�</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">�ŷ��� 
                                    ����</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">������</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="#CC3300">���� 
                                    90%</font><font color="blue"> ���� 100% ��� 100%</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">����(30���)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">$max7</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p><span style="font-size:9pt;">����� �ҼҸ�(60���)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">50</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="65" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">����</span></p>
                                </td>
                                <td width="300" height="65" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">������� 
                                    ��Ʋ�� �ְ��� �����Դϴ�. ���ݷ�,�����,�����ݷ� 
                                    ���� ����� ������ �ɷ�ġ�� �ݿ��� �˴ϴ�. 
                                    ������ ��Ʋ�� ������ �����Դϴ�. ���� ������������ 
                                    ����� �� �ֽ��ϴ�.</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="432" height="22" colspan="2" bgcolor="black">
<form action="$COMMAND" method="POST">
                                        <p align="right"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<input type=text name=num value=$get_sol size=4>���� 
$no_list<input type=hidden name=type value=7><input type=hidden name=mode value=10><input type=submit value="����Ѵ�">
</form>
                                </td>
                            </tr>
                        </table><br>
                        <table align="center" border="1" cellspacing="0" width="438" bordercolordark="white" bordercolorlight="black">
                            <tr>
                                <td width="432" height="35" colspan="2" bgcolor="black">
                                    <p align="center"><font color="$by9"><span style="font-size:10pt;"><b><a name="10"></a>�ڳ�����</b></span></font></p>
                                </td>
                            </tr>
                                 <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">����</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">�⺴�迭</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">���ݷ�</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">�ڡڡڡڡڡ�(90)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">�����</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">�ڡڡڡڡڡ�(90)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">�����ݷ�</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">�ڡڡڡڡ�(75)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">������</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="#00CC00">���� 
                                    120%</font><font color="blue"> </font><font color="#CC3300">���� 
                                    80% ��� 70%</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">����(30���)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">$max8</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p><span style="font-size:9pt;">����� �ҼҸ�(60���)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">60</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="65" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">����</span></p>
                                </td>
                                <td width="300" height="65" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">�ڳ������� 
                                    ��������� ¡�������� �����Դϴ�. ������ 
                                    ���ݷ�,�����,�����ݷ��� �߱��� ������ �ڶ��մϴ�. 
                                    ���� �������� ���� Ÿ�� �ҼҸ� �ؽ��մϴ�.</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="432" height="22" colspan="2" bgcolor="black">
<form action="$COMMAND" method="POST">
                                        <p align="right"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<input type=text name=num value=$get_sol size=4>���� 
$no_list<input type=hidden name=type value=8><input type=hidden name=mode value=10><input type=submit value="����Ѵ�">
</form>
                                </td>
                            </tr>
                        </table><br>
                        <table align="center" border="1" cellspacing="0" width="438" bordercolordark="white" bordercolorlight="black">
                            <tr>
                                <td width="432" height="35" colspan="2" bgcolor="black">
                                    <p align="center"><font color="$by10"><span style="font-size:10pt;"><b><a name="11"></a>��Ǻ�</b></span></font></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">����</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">�����迭</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">���ݷ�</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">�ڡڡ�(45)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">�����</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">�ڡڡ�(45)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">�����ݷ�</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">�ڡ�(30)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">������</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="#CC3300">���� 80% ���� 80%</font><font color="blue"> </font><font color="#00CC00">��� 130%</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">����(30���)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">$max9</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p><span style="font-size:9pt;">����� �ҼҸ�(60���)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">30</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="65" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">����</span></p>
                                </td>
                                <td width="300" height="65" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">��Ǻ��� 
                                    ��ǿ��� ���� �� �ִ� ��� ���� ���� Ưȭ 
                                    �����Դϴ�. ���ݷ� ������� ���庸���� �ٸ� 
                                    �� ������ ����������� ���� 2���� �������� 
                                    �ٽ��ϴ�. �Դٰ� ����������� ��ų ���ź����� 
                                    ����� �� �ְ� �˴ϴ�.</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="432" height="22" colspan="2" bgcolor="black">
<form action="$COMMAND" method="POST">
                                        <p align="right"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<input type=text name=num value=$get_sol size=4>���� 
$no_list<input type=hidden name=type value=9><input type=hidden name=mode value=10><input type=submit value="����Ѵ�">
</form>
                                </td>
                            </tr>
                        </table><br>
                        <table align="center" border="1" cellspacing="0" width="438" bordercolordark="white" bordercolorlight="black">
                            <tr>
                                <td width="432" height="35" colspan="2" bgcolor="black">
                                    <p align="center"><font color="$by11"><span style="font-size:10pt;"><b><a name="12"></a>ö�⺴</b></span></font></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">����</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">�⺴�迭</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">���ݷ�</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">�ڡڡڡڡ�(75)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">�����</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">�ڡڡڡ�(60)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">�����ݷ�</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">�ڡ�(30)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">������</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="#00CC00">���� 
                                    130%</font><font color="blue"> </font><font color="#CC3300">���� 70% ��� 60%</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">����(30���)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">$max10</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p><span style="font-size:9pt;">����� �ҼҸ�(60���)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">40</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="65" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">����</span></p>
                                </td>
                                <td width="300" height="65" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">ö�⺴�� 
                                    �Ϻ� �Ϻ� ���ÿ����� ������ �����մϴ�. 
                                    ������ �⺴���� ö���� ������ ������ ��ȭ�Ǿ����ϴ�. 
                                    �������� �߱��� ������ �ڶ��մϴ�.</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="432" height="22" colspan="2" bgcolor="black">
<form action="$COMMAND" method="POST">
                                        <p align="right"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<input type=text name=num value=$get_sol size=4>���� 
$no_list<input type=hidden name=type value=10><input type=hidden name=mode value=10><input type=submit value="����Ѵ�">
</form>
                                </td>
                            </tr>
                        </table><br>
                        <table align="center" border="1" cellspacing="0" width="438" bordercolordark="white" bordercolorlight="black">
                            <tr>
                                <td width="432" height="35" colspan="2" bgcolor="black">
                                    <p align="center"><font color="$by12"><span style="font-size:10pt;"><b><a name="13"></a>ȭ��</b></span></font></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">����</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">�⺴�迭</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">���ݷ�</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">�ɷ�ġ �߿� �� ���� ������</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">�����</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">�ɷ�ġ �߿� �� ���� ������</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">�����ݷ�</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">�ɷ�ġ �߿� �� ���� ������</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">������</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="#CC3300">���� 
                                    90% ���� 90%</font><font color="blue"> ��� 100%</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">����(30���)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">$max11</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p><span style="font-size:9pt;">����� �ҼҸ�(60���)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">30</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="65" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">����</span></p>
                                </td>
                                <td width="300" height="65" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">ȭ���� 
                                    ������������� ���� �� �ִ� �����Դϴ�. 
                                    ������ �����ϱ� ������ �� �� �� ������ ���ݷ�,�����,�����ݷ��� 
                                    ��ȭ�մϴ�.</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="432" height="22" colspan="2" bgcolor="black">
<form action="$COMMAND" method="POST">
                                        <p align="right"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<input type=text name=num value=$get_sol size=4>���� 
$no_list<input type=hidden name=type value=11><input type=hidden name=mode value=10><input type=submit value="����Ѵ�">
</form>
                                </td>
                            </tr>
                        </table><br>
                        <table align="center" border="1" cellspacing="0" width="438" bordercolordark="white" bordercolorlight="black">
                            <tr>
                                <td width="432" height="35" colspan="2" bgcolor="black">
                                    <p align="center"><font color="$by13"><span style="font-size:10pt;"><b><a name="14"></a>�߼���</b></span></font></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">����</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">�ͺ��迭</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">���ݷ�</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">��(0)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">�����</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">��(0)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">�����ݷ�</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">�ڡڡڡڡڡڡڡڡڡ�(150)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">������</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="blue">���� 
                                    100% ���� 100% ��� 100%</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">����(30���)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">$max12</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p><span style="font-size:9pt;">����� �ҼҸ�(60���)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">40</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="65" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">����</span></p>
                                </td>
                                <td width="300" height="65" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">�߼��Ŵ� 
                                    �����ɿ� �־� �ʼ����� �����Դϴ�. ���� 
                                    ���� ����߸��µ� �־� �߼��Ÿ�ŭ �ż��� 
                                    ������ ���� �����Դϴ�. ������ ������������ 
                                    ����� ��� ��Ÿ���ϴ�.</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="432" height="22" colspan="2" bgcolor="black">
<form action="$COMMAND" method="POST">
                                        <p align="right"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<input type=text name=num value=$get_sol size=4>���� 
$no_list<input type=hidden name=type value=12><input type=hidden name=mode value=10><input type=submit value="����Ѵ�">
</form>
                                </td>
                            </tr>
                        </table><br>
                        <table align="center" border="1" cellspacing="0" width="438" bordercolordark="white" bordercolorlight="black">
                            <tr>
                                <td width="432" height="35" colspan="2" bgcolor="black">
                                    <p align="center"><font color="$by14"><span style="font-size:10pt;"><b><a name="15"></a>Ȳ����</b></span></font></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">����</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">�����迭</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">���ݷ�</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">�ŷ��� 
                                    ����</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">�����</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">��(15)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">�����ݷ�</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">�ŷ�/2 
                                    ����</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">������</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="#00CC00">���� 
                                    110%</font><font color="blue"> ���� 100% </font><font color="#CC3300">��� 80%</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">����(30���)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">$max13</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p><span style="font-size:9pt;">����� �ҼҸ�(60���)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">30</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="65" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">����</span></p>
                                </td>
                                <td width="300" height="65" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">���忡�� 
                                    �űͺ��� �ִٸ� ���忡�� Ȳ������ �ֽ��ϴ�.&nbsp;���ݷ¿� 
                                    �ŷ��� ����Ǳ� ������ ���忡�Դ� Ư���� 
                                    �Ÿ�Ʈ�� �ֽ��ϴ�. �Դٰ� �űͺ����ٵ� �α� 
                                    ������ �δ���� ����� �� �ֽ��ϴ�.</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="432" height="22" colspan="2" bgcolor="black">
<form action="$COMMAND" method="POST">
                                        <p align="right"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<input type=text name=num value=$get_sol size=4>���� 
$no_list<input type=hidden name=type value=13><input type=hidden name=mode value=10><input type=submit value="����Ѵ�">
</form>
                                </td>
                            </tr>
                        </table><br>
                        <table align="center" border="1" cellspacing="0" width="438" bordercolordark="white" bordercolorlight="black">
                            <tr>
                                <td width="432" height="35" colspan="2" bgcolor="black">
                                    <p align="center"><font color="$by15"><span style="font-size:10pt;"><b><a name="16"></a>�����</b></span></font></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">����</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">â���迭</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">���ݷ�</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">������ 
                                    ����</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">�����</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">��(15)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">�����ݷ�</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">����/2 
                                    ����</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">������</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="#CC3300">���� 
                                    90%</font><font color="blue"> ���� 100% </font><font color="#00CC00">��� 110%</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">����(30���)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">$max15</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p><span style="font-size:9pt;">����� �ҼҸ�(60���)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">30</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="65" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">����</span></p>
                                </td>
                                <td width="300" height="65" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">������� 
                                    ȸ�輺������ ���� �� �ִ� ���� Ưȭ�����Դϴ�. 
                                    ���� ����+���ݷ� ������ ���꿡�� ���ֵǴ� 
                                    ���ݷ��� ������ �����Դϴ�.</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="432" height="22" colspan="2" bgcolor="black">
<form action="$COMMAND" method="POST">
                                        <p align="right"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<input type=text name=num value=$get_sol size=4>���� 
$no_list<input type=hidden name=type value=15><input type=hidden name=mode value=10><input type=submit value="����Ѵ�">
</form>
                                </td>
                            </tr>
                        </table><br>
                        <table align="center" border="1" cellspacing="0" width="438" bordercolordark="white" bordercolorlight="black">
                            <tr>
                                <td width="432" height="35" colspan="2" bgcolor="black">
                                    <p align="center"><font color="$by16"><span style="font-size:10pt;"><b><a name="17"></a>�ļ���</b></span></font></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">����</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">�ͺ��迭</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">���ݷ�</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">��(0)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">�����</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">��(0)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">�����ݷ�</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">�ڡڡڡڡ�(75) 
                                    / ���ü�����:��(10)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">������</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="blue">���� 
                                    100% ���� 100% ��� 100%</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">����(30���)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">$max17</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p><span style="font-size:9pt;">����� �ҼҸ�(60���)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">40</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="65" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">����</span></p>
                                </td>
                                <td width="300" height="65" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">�ļ����� 
                                    �߼��ſʹ� �޸� ������ ������ �Ӹ� �ƴ϶� 
                                    ���ü��� �ı��մϴ�. �ַ� �����ϱⰡ ���� 
                                    �ʴ� Ư���̳� �뼺�� ����Ͽ� �󼺼������ 
                                    ���ݷ��� ��ȭ��Ű�µ� Ź���մϴ�.</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="432" height="22" colspan="2" bgcolor="black">
<form action="$COMMAND" method="POST">
                                        <p align="right"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<input type=text name=num value=$get_sol size=4>���� 
$no_list<input type=hidden name=type value="17"><input type=hidden name=mode value=10><input type=submit value="����Ѵ�">
</form>
                                </td>
                            </tr>
                        </table>
			<br>
                        <table align="center" border="1" cellspacing="0" width="438" bordercolordark="white" bordercolorlight="black">
                            <tr>
                                <td width="432" height="35" colspan="2" bgcolor="black">
                                    <p align="center"><font color="$by17"><span style="font-size:10pt;"><b><a name="18"></a>�غ�</b></span></font></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">����</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">â���迭</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">���ݷ�</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">����� 
                                    ����</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">�����</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">��(0)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">�����ݷ�</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">��(15)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">������</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="blue">���� 
                                    100% </font><font color="#CC3300">���� 80%</font><font color="blue"> </font><font color="#00CC00">��� 110%</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">����(30���)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">$max18</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p><span style="font-size:9pt;">����� �ҼҸ�(60���)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">40</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="65" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">����</span></p>
                                </td>
                                <td width="300" height="65" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">���� 
                                    ����ϴ� �δ��Դϴ�. ��ַ��� ���ݷ¿� ����Ǿ� 
                                    �߱��� ������ �ڶ��մϴ�. ������ �������� 
                                    �����ϰ�� �״��� ���� ������ �ʽ��ϴ�.</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="432" height="22" colspan="2" bgcolor="black">
<form action="$COMMAND" method="POST">
                                        <p align="right"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<input type=text name=num value=$get_sol size=4>���� 
$no_list<input type=hidden name=type value="18"><input type=hidden name=mode value=10><input type=submit value="����Ѵ�">
</form>
                                </td>
                            </tr>
                        </table><br>
                        <table align="center" border="1" cellspacing="0" width="438" bordercolordark="white" bordercolorlight="black">
                            <tr>
                                <td width="432" height="35" colspan="2" bgcolor="black">
                                    <p align="center"><font color="$by18"><span style="font-size:10pt;"><b><a name="19"></a>����</b></span></font></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">����</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">�����迭</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">���ݷ�</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">�ڡڡڡ�(60)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">�����</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">�ڡڡ�(45)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">�����ݷ�</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">�ڡ�(30)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">������</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="#CC3300">���� 80% </font><font color="#00CC00">���� 130%</font><font color="blue"> </font><font color="#CC3300">��� 80%</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">����(30���)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">$max19</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p><span style="font-size:9pt;">����� �ҼҸ�(60���)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">30</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="65" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">����</span></p>
                                </td>
                                <td width="300" height="65" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">���󿡼� 
                                    ���������� �ο�� �����Դϴ�. ������ ��α� 
                                    ������ ���ݷ°� ������� �������� �������� 
                                    ������ ������ ��� ���������� �Ҹ��� �����Դϴ�.</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="432" height="22" colspan="2" bgcolor="black">
<form action="$COMMAND" method="POST">
                                        <p align="right"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<input type=text name=num value=$get_sol size=4>���� 
$no_list<input type=hidden name=type value="19"><input type=hidden name=mode value=10><input type=submit value="����Ѵ�">
</form>
                                </td>
                            </tr>
                        </table>
			<br>
                        <table align="center" border="1" cellspacing="0" width="438" bordercolordark="white" bordercolorlight="black">
                            <tr>
                                <td width="432" height="35" colspan="2" bgcolor="black">
                                    <p align="center"><font color="$by19"><span style="font-size:10pt;"><b><a name="20"></a>����</b></span></font></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">����</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">�����迭</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">���ݷ�</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">�ڡ�(30)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">�����</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">�ڡ�(30)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">�����ݷ�</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">�ڡڡ�(45)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">������</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="blue">���� 
                                    100% </font><font color="#00CC00">���� 110%</font><font color="blue"> </font><font color="#CC3300">��� 90%</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">����(30���)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">$max20</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p><span style="font-size:9pt;">����� �ҼҸ�(60���)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">20</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="65" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">����</span></p>
                                </td>
                                <td width="300" height="65" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">������ ������ �������� �����ϴ� �����Դϴ�. ���ݷ°� ������� ���庸�����ؿ� �Ұ������� ������ �����ϴ� �ɷ��� ������ �ֽ��ϴ�. ������ 2000���̻��� 100% �������� �� ���ϴ� ������ �������� ������ ����Ȯ���� ����մϴ�. ���� ������� �� ����δ��� ���ݷ��� �ڽ��� ���ݷ��� 2���̻��� ��� ���� ������� �ڽ��� ���ݷ����� ī��(Copy)�մϴ�.</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="432" height="22" colspan="2" bgcolor="black">
<form action="$COMMAND" method="POST">
                                        <p align="right"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<input type=text name=num value=$get_sol size=4>���� 
$no_list<input type=hidden name=type value="20"><input type=hidden name=mode value=10><input type=submit value="����Ѵ�">
</form>
                                </td>
                            </tr>
                        </table>			<br>
<form action="$FILE_STATUS" method="post">
                            <p align="center"><input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="���ƿ´�"></center></form>
                    </td>
                </tr>
                <tr>
                    <td width="677">
                        <p><img src="$IMG/law2.gif" width="700" height="22" border="0"></p>
                    </td>
                </tr>
            </table>
        </td>
    </tr>
    <tr>
        <td width="937">
            <p><img src="$IMG/down.gif" width="950" height="26" border="0"></p>
        </td>
    </tr>
</table>
</body>

EOM
&FOOTER;
exit;

}
1;