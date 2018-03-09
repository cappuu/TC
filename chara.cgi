#!/usr/bin/perl

require 'jcode.pl';
require './ini_file/index.ini';
require 'suport.cgi';

&DECODE;
&BODY;

sub BODY {



	if ($in{'id'} =~ /[^0-9a-zA-Z]/){
		&ERR2("�����Դϴ�.");
	}

	&TOWN_DATA_OPEN("$kpos");




	open(IN,"./charalog/main/$in{'id'}.cgi") or &ERR2('ID�� �н��� �ùٸ��� �ʽ��ϴ�!');
	@CN_DATA = <IN>;
	close(IN);

	($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$kskill,$kpoint,$kct,$klevel,$kexp,$kcodea,$kcodeb,$kqpoint) = split(/<>/,$CN_DATA[0]);
	($kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,$bo_ex,$gi_ex,$ch_ex,$gu_ex,$go_ex) = split(/,/,$ksub1);
	
	$levelup = int(200 * (1+($klevel*0.1)));

	foreach(@TOWN_DATA){
		($zzname,$zzcon,$zznum,$zznou,$zzsyo,$zzshiro,$zznou_max,$zzsyo_max,$zzshiro_max,$zzpri,$zzx,$zzy,$zzsouba,$zzdef_att,$zzsub1,$zzsub2,$z[0],$z[1],$z[2],$z[3],$z[4],$z[5],$z[6],$z[7],$zzname1,$zzname2,$zzbong1,$zzbong2,$zzbong3)=split(/<>/);
		if($kid eq "$zzbong1" || $kid eq "$zzbong2" || $kid eq "$zzbong3"){
			$bongto = "$zzname";
		}
	}

	$bos = int($bo_ex/3);
	if($bo_ex < 3){$bos = 0;}
	$gis = int($gi_ex/3);
	if($gi_ex < 3){$gis = 0;}
	$chs = int($ch_ex/3);
	if($ch_ex < 3){$chs = 0;}
	$gus = int($gu_ex/3);
	if($gu_ex < 3){$gus = 0;}

	if($go_ex < 500){
		$sangtae = "<font color=301ED8>�ǰ�</font>";
	}elsif($go_ex <1000 && $go_ex > 499){
		$sangtae = "<font color=000000>����</font>";
	}elsif($go_ex < 1250 && $go_ex > 999){
		$sangtae = "<font color=730C86>����</font>";
	}elsif($go_ex < 1500 && $go_ex > 1249){
		$sangtae = "<font color=C51B4B>����</font>";
	}elsif($go_ex <1700 && $go_ex > 1499){
		$sangtae = "<font color=FF0000>����</font>";
	}

	if($kskill =~ /Aa/){
		$skill_list .= "�������";
	}
	if($kskill =~ /Ab/){
		$skill_list .= "���ŷ���";
	}
	if($kskill =~ /Ac/){
		$skill_list .= "��������";
	}
	if($kskill =~ /Ba/){
		$skill_list .= "�������";
	}
	if($kskill =~ /Bb/){
		$skill_list .= "�����ϡ�";
	}
	if($kskill =~ /Bc/){
		$skill_list .= "����롷";
	}
	if($kskill =~ /Ca/){
		$skill_list .= "�������";
	}
	if($kskill =~ /Cb/){
		$skill_list .= "��ȸ�ǡ�";
	}
	if($kskill =~ /Cc/){
		$skill_list .= "��������";
	}
	if($kskill =~ /Da/){
		$skill_list .= "���缺��";
	}
	if($kskill =~ /Db/){
		$skill_list .= "���𺴡�";
	}
	if($kskill =~ /Dc/){
		$skill_list .= "����ġ��";
	}
	if($kskill =~ /Ea/){
		$skill_list .= "���Ʒá�";
	}
	if($kskill =~ /Eb/){
		$skill_list .= "��������";
	}
	if($kskill =~ /Ec/){
		$skill_list .= "��������";
	}
	if($kskill =~ /Fa/){
		$skill_list .= "���νɡ�";
	}
	if($kskill =~ /Fb/){
		$skill_list .= "���ŷᡷ";
	}
	if($kskill =~ /Fc/){
		$skill_list .= "��������";
	}
	if($kskill =~ /Ga/){
		$skill_list .= "����硷";
	}
	if($kskill =~ /Gb/){
		$skill_list .= "��������";
	}
	if($kskill =~ /Gc/){
		$skill_list .= "���ϼ���";
	}




	&COUNTRY_DATA_OPEN("$kcon");
	if($xking eq "$kid"){
		$rank_mes = "����";
	}elsif($x0 eq "$kid"){
		$rank_mes = "����";
	}elsif($x1 eq "$kid"){
		$rank_mes = "���屺";
	}elsif($x2 eq "$kid"){
		$rank_mes = "ǥ���屺";
	}elsif($x3 eq "$kid"){
		$rank_mes = "�ű��屺";
	}elsif($x4 eq "$kid"){
		$rank_mes = "���屺";
	}elsif($x5 eq "$kid"){
		$rank_mes = "�����屺";
	}elsif($x6 eq "$kid"){
		$rank_mes = "�����屺";
	}elsif($x7 eq "$kid"){
		$rank_mes = "�����屺";
	}elsif($x8 eq "$kid"){
		$rank_mes = "�����屺";
	}elsif($x9 eq "$kid"){
		$rank_mes = "�����屺";
	}elsif($x10 eq "$kid"){
		$rank_mes = "�����屺";
	}elsif($x11 eq "$kid"){
		$rank_mes = "�����屺";
	}elsif($x12 eq "$kid"){
		$rank_mes = "�����屺";
	}elsif($x13 eq "$kid"){
		$rank_mes = "�ȵ��屺";
	}elsif($x14 eq "$kid"){
		$rank_mes = "�ȼ��屺";
	}elsif($x15 eq "$kid"){
		$rank_mes = "�ȳ��屺";
	}elsif($x16 eq "$kid"){
		$rank_mes = "�Ⱥ��屺";
	}elsif($x17 eq "$kid"){
		$rank_mes = "�»�";
	}elsif($x18 eq "$kid"){
		$rank_mes = "�º�";
	}elsif($x19 eq "$kid"){
		$rank_mes = "�»�";
	}elsif($x20 eq "$kid"){
		$rank_mes = "�º�";
	}elsif($x21 eq "$kid"){
		$rank_mes = "�����";
	}elsif($x22 eq "$kid"){
		$rank_mes = "����";
	}elsif($x23 eq "$kid"){
		$rank_mes = "�̺λ�";
	}elsif($x24 eq "$kid"){
		$rank_mes = "ȣ�λ�";
	}elsif($x25 eq "$kid"){
		$rank_mes = "���λ�";
	}elsif($x26 eq "$kid"){
		$rank_mes = "���λ�";
	}else{$rank_mes = "���";
	}




	&CHARA_ITEM_OPEN;

	$kstrplus = $itemstr[$karm] + $itemstr[$kbook];
	$kintplus = $itemint[$karm] + $itemint[$kbook];
	$kleaplus = $itemlea[$karm] + $itemlea[$kbook];
	$kchaplus = $itemcha[$karm] + $itemcha[$kbook];
	$kstrtotal = $kstrt;
	$kinttotal = $kintt;
	$kleatotal = $kleat;
	$kchatotal = $kchat;

	if( $karm > 0 ){
		$item_list .= $itemname[$karm] . ", ";
	}
	if( $kbook > 0 ){
		$item_list .= $itemname[$kbook] . ", ";
	}
	if( $item_list ne "" ){
		$item_list = substr($item_list,0,length($item_list)-2);
	}

	if( $kstrtotal > 100 ){
		$len_kstr = 100;
		$over = $kstrtotal-100;
	}else{
		$len_kstr = $kstrtotal;
		$len_kstr2 = '<img src="$img/bar2.gif" width="'.(100 - $len_kstr).'" height="5">';
	}
	if( $kinttotal > 100 ){
		$len_kint = 100;
		$over = $kinttotal-100;
	}else{
		$len_kint = $kinttotal;
		$len_kint2 = '<img src="$img/bar2.gif" width="'.(100 - $len_kint).'" height="5">';
	}
	if( $kleatotal > 100 ){
		$len_klea = 100;
		$over = $kleatotal-100;
	}else{
		$len_klea = $kleatotal;
		$len_klea2 = '<img src="$img/bar2.gif" width="'.(100 - $len_klea).'" height="5">';
	}
	if( $kchatotal > 100 ){
		$len_kcha = 100;
		$over = $kchatotal-100;
	}else{
		$len_kcha = $kchatotal;
		$len_kcha2 = '<img src="$img/bar2.gif" width="'.(100 - $len_kcha).'" height="5">';
	}
	if($go_ex>1700 ){
		$len_go = int(1700/17);
		$over = int($go_ex-1700/17);
	}else{
		$len_go = int($go_ex/17);
		$len_go2 = '<img src="$img/bar2.gif" width="'.(100 - $len_go).'" height="5">';
	}

	if( $kstrplus > 0 ){
		$kstrplusmes = "(+$kstrplus)";
	}
	if( $kintplus > 0 ){
		$kintplusmes = "(+$kintplus)";
	}
	if( $kleaplus > 0 ){
		$kleaplusmes = "(+$kleaplus)";
	}
	if( $kchaplus > 0 ){
		$kchaplusmes = "(+$kchaplus)";
	}
	if( $bo_ex > 0 ){
		$bomes = "(+$kchaplus)";
	}


	if( $kcon != 0 ){
		$con_name = "$cou_name[$kcon]��";
	}else{
		$con_name = "���Ҽ�";
	}

	open(IN,"./charalog/history/$in{'id'}.cgi") or &ERR("������ ������ ������ �ʽ��ϴ�.");
	@HISTORY_DATA = <IN>;
	close(IN);

	print "Cache-Control: no-cache\n";
	print "Pragma: no-cache\n";
	print "Content-type: text/html\n\n";

print <<"EOM";
<html>
<head>
<META HTTP-EQUIV="Content-type" CONTENT="text/html; charset=euc-kr">
<title>ĥ������ $kname ����</title>
<STYLE type="text/css">
<!--
BODY,TR,TD,TH{
font-size:9pt;
line-height: 10pt;
}
.text { font-size: 9pt; line-height: 14pt; }
.8pttext { font-size: 8pt; line-height: 14pt; }
-->
</STYLE>
</head>
<body bgcolor="#F0E8E0" text="" link="#993300" vlink="#993300" alink="#993300" topmargin="0" leftmargin="0" marginwidth="0" marginheight="0" onload="window.focus()">
	<TABLE width="100%" bgcolor=$ELE_BG[$cou_ele[$kcon]] cellpadding="2" cellspacing="1" align="center">
	<TR><TH colspan=7 bgcolor=$ELE_BG[$cou_ele[$kcon]]><font color=$ELE_C[$cou_ele[$kcon]]>$rank_mes $kname</font></TH></TR>

	<TR bgcolor=$ELE_C[$cou_ele[$kcon]]>
	<TD width=64 rowspan="5">
		<img src=$IMG/$kchara.gif>
	</TD>
	<TD width=40>�Ҽ�</TD>
	<TD width=120>$con_name</TD>
	</TR>
	<TR bgcolor=$ELE_C[$cou_ele[$kcon]]>
	<TD>����</TD>
	<TD>$kbank</TD>
	</TR>
	<TR bgcolor=$ELE_C[$cou_ele[$kcon]]>
	<TD>����</TD>
	<TD>$klevel ($kexp / $levelup)<br>�Ѱ���ġ:$kclass<br>����ġ:$kcex</TD>
	</TR>
	<TR bgcolor=$ELE_C[$cou_ele[$kcon]]>
	<TD>����</TD>
	<TD>$town_name[$kct]</TD>
	</TR>
	<TR bgcolor=$ELE_C[$cou_ele[$kcon]]>
	<TD>����</TD>
	<TD>$bongto</TD>
	</TR>
	<TR>
	<TD colspan="3" bgcolor=$ELE_C[$cou_ele[$kcon]]>

		<TABLE WIDTH="100%">
		<TR>
		<TD>����</TD>
		<TD align="right"><b>$kstrtotal</b></TD>
		<TD align="left"><b>$kstrplusmes</b></TD>
		<TD><img src="$IMG/bar.gif" width="$len_kstr" height="8">$len_kstr2</TD>
		</TR>
		<TR>
		<TD>����</TD>
		<TD align="right"><b>$kinttotal</b></TD>
		<TD align="left"><b>$kintplusmes</b></TD>
		<TD><img src="$IMG/bar.gif" width="$len_kint" height="8">$len_kint2</TD>
		</TR>
		<TR>
		<TD>��ַ�</TD>
		<TD align="right"><b>$kleatotal</b></TD>
		<TD align="left"><b>$kleaplusmes</b></TD>
		<TD><img src="$IMG/bar.gif" width="$len_klea" height="8">$len_klea2</TD>
		</TR>
		<TR>
		<TD>�ŷ�</TD>
		<TD align="right"><b>$kchatotal</b></TD>
		<TD align="left"><b>$kchaplusmes</b></TD>
		<TD><img src="$IMG/bar.gif" width="$len_kcha" height="8">$len_kcha2</TD>
		</TR>

		</TABLE>

	</TD>
	</TR>
	<TR>
	<TD colspan="3" bgcolor=$ELE_C[$cou_ele[$kcon]]>
	<TABLE WIDTH="100%">
	<TD width=40>�Ƿε�</TD>
	<TD width=44 align="right"><b>$sangtae</b></TD>
	<TD width=100>
            <table cellpadding="0" cellspacing="0" WIDTH="100%" background="$IMG/bar3.gif">
                <tr>
                    <td>
		<img src="$IMG/bar2.gif" width="$len_go" height="8">$len_go2</TD>
                    </td>
                </tr>
            </table>
	<td></td>
	</TR>
	</TABLE>
	</td>
	</tr>
	<tr>
	<td colspan="3" width=100%>
<table width=100% bgcolor=$ELE_C[$cou_ele[$kcon]]>
    <tr>
        <td colspan="4" bgcolor=$ELE_BG[$cou_ele[$kcon]]>
            <p align="center"><font color=$ELE_C[$cou_ele[$kcon]]><b>��������</b></font></p>
        </td>
    </tr>
    <tr>
        <td width="25%" height="7" bgcolor=$ELE_BG[$cou_ele[$kcon]]>
            <p align="center"><font color=$ELE_C[$cou_ele[$kcon]]>�����迭</font></p>
        </td>
        <td width="25%" height="7" bgcolor=$ELE_BG[$cou_ele[$kcon]]>
            <p align="center"><font color=$ELE_C[$cou_ele[$kcon]]>�⺴�迭</font></p>
        </td>
        <td width="25%" height="7" bgcolor=$ELE_BG[$cou_ele[$kcon]]>
            <p align="center"><font color=$ELE_C[$cou_ele[$kcon]]>â���迭</font></p>
        </td>
        <td width="25%" height="7" bgcolor=$ELE_BG[$cou_ele[$kcon]]>
            <p align="center"><font color=$ELE_C[$cou_ele[$kcon]]>�ͺ��迭</font></p>
        </td>
    </tr>
    <tr>
        <td>
            <p align="center">Lv.$bos</p>
        </td>
        <td>
            <p align="center">Lv.$gis</p>
        </td>
        <td>
            <p align="center">Lv.$chs</p>
        </td>
        <td>
            <p align="center">Lv.$gus</p>
        </td>
    </tr>
</table>
	</td>
	</tr>
	</TABLE>
EOM
	if( $kskill ne "" ){
print <<"EOM";
	<TABLE width="100%" bgcolor=$ELE_BG[$cou_ele[$kcon]] cellpadding="2" cellspacing="1" align="center">
	<TR><TH colspan=7 bgcolor=$ELE_BG[$cou_ele[$kcon]]><font color=$ELE_C[$cou_ele[$kcon]]>����Ư��</font></TH></TR>
	<TR>
	<TD bgcolor=$ELE_C[$cou_ele[$kcon]] class="text">$skill_list</TD>
	</TR>
	</TABLE>
EOM

	}

	open(IN,"$QUEST_DATA");
	@QUEST_DATA = <IN>;
	close(IN);

	foreach(@QUEST_DATA){
		($qnum,$qcode,$qface,$qname,$qlevel,$quest,$qlimit,$qtalka,$qtalkb,$qtalkc,$qgold,$qrice,$qstr,$qint,$qlea,$qcha,$qcex,$qexp,$qseal) = split(/<>/);
		if($kcodea =~ /$qcode/){
		$quest_list = "<b>[ $quest ]</b><br>$qseal : $kqpoint/$qlimit";
		}
	}
	if( $kcodea ne "" ){
print <<"EOM";
	<TABLE width="100%" bgcolor=$ELE_BG[$cou_ele[$kcon]] cellpadding="2" cellspacing="1" align="center">
	<TR><TH colspan=7 bgcolor=$ELE_BG[$cou_ele[$kcon]]><font color=$ELE_C[$cou_ele[$kcon]]>�������� ����Ʈ</font></TH></TR>
	<TR>
	<TD bgcolor=$ELE_C[$cou_ele[$kcon]] class="text">$quest_list</TD>
	</TR>
	</TABLE>
EOM
	}
	if( $kmes ne "" ){
print <<"EOM";
	<TABLE width="100%" cellpadding="2" cellspacing="1" align="center">
	<TR><TH colspan=7 bgcolor=$ELE_BG[$cou_ele[$kcon]]><font color=$ELE_C[$cou_ele[$kcon]]>�ڱ�Ұ�</font></TH></TR>
	<TR>
	<TD bgcolor=$ELE_C[$cou_ele[$kcon]] class="text">$kmes</TD>
	</TR>
	</TABLE>
EOM
	}
print <<"EOM";
	<TABLE width="100%" bgcolor=$ELE_BG[$cou_ele[$kcon]] cellpadding="2" cellspacing="1" align="center">
	<TR><TH colspan=7 bgcolor=$ELE_BG[$cou_ele[$kcon]]><font color=$ELE_C[$cou_ele[$kcon]]>$kname ����</font></TH></TR>
	<TR>
	<TD bgcolor=$ELE_C[$cou_ele[$kcon]] class="text">
EOM
	foreach(@HISTORY_DATA){
		($date,$value) = split(/: /,$_);
		print "<span class=8pttext>".$date.":</span>".$value."<br>";
	}
print <<"EOM";
	</TD>
	</TR>
	</TABLE>
</body>
</html>
EOM

}
