#!/usr/bin/perl

require 'jcode.pl';
require './ini_file/index.ini';
require 'suport.cgi';

if($MENTE) { &ERR("�ε����Դϴ�. ��ø� ��ٷ� �ֽʽÿ�."); }
&DECODE;
&BONGTOG_D;


sub BONGTOG_D {

	&CHARA_MAIN_OPEN;
	open(IN,"./charalog/log/$kid.cgi");
	@LOG_DATA = <IN>;
	close(IN);
	&COUNTRY_DATA_OPEN($kcon);

	open(IN,"$TOWN_LIST") or &ERR("������ ������ ������ �ʽ��ϴ�.");
	@TOWN_DATA = <IN>;
	close(IN);

	if($in{'bongto'} eq ""){&ERR("������ ���佽���� �Է����� �ʾҽ��ϴ�.");}

	$num1=0;
	foreach(@TOWN_DATA){
	($zname,$zcon,$znum,$znou,$zsyo,$zshiro,$znou_max,$zsyo_max,$zshiro_max,$zpri,$zx,$zy,$zsouba,$zdef_att,$zsub1,$zsub2,$z[0],$z[1],$z[2],$z[3],$z[4],$z[5],$z[6],$z[7],$zname1,$zname2,$zbong1,$zbong2,$zbong3)=split(/<>/);
	if($in{'numd'} eq $num1){
	if($in{'bongto'} eq "1"){
		$zbong1 = "";
	splice(@TOWN_DATA,$in{'numd'},1,"$zname<>$zcon<>$znum<>$znou<>$zsyo<>$zshiro<>$znou_max<>$zsyo_max<>$zshiro_max<>$zpri<>$zx<>$zy<>$zsouba<>$zdef_att<>$zsub1<>$zsub2<>$z[0]<>$z[1]<>$z[2]<>$z[3]<>$z[4]<>$z[5]<>$z[6]<>$z[7]<>$zname1<>$zname2<>$zbong1<>$zbong2<>$zbong3<>\n");
	open(OUT,">$TOWN_LIST") or &ERR('TOWN �����͸� ������ �� �����ϴ�.');
	print OUT @TOWN_DATA;
	close(OUT);
	}elsif($in{'bongto'} eq "2"){
		$zbong2 = "";
	splice(@TOWN_DATA,$in{'numd'},1,"$zname<>$zcon<>$znum<>$znou<>$zsyo<>$zshiro<>$znou_max<>$zsyo_max<>$zshiro_max<>$zpri<>$zx<>$zy<>$zsouba<>$zdef_att<>$zsub1<>$zsub2<>$z[0]<>$z[1]<>$z[2]<>$z[3]<>$z[4]<>$z[5]<>$z[6]<>$z[7]<>$zname1<>$zname2<>$zbong1<>$zbong2<>$zbong3<>\n");
	open(OUT,">$TOWN_LIST") or &ERR('TOWN �����͸� ������ �� �����ϴ�.');
	print OUT @TOWN_DATA;
	close(OUT);
	}elsif($in{'bongto'} eq "3"){
		$zbong3 = "";
	splice(@TOWN_DATA,$in{'numd'},1,"$zname<>$zcon<>$znum<>$znou<>$zsyo<>$zshiro<>$znou_max<>$zsyo_max<>$zshiro_max<>$zpri<>$zx<>$zy<>$zsouba<>$zdef_att<>$zsub1<>$zsub2<>$z[0]<>$z[1]<>$z[2]<>$z[3]<>$z[4]<>$z[5]<>$z[6]<>$z[7]<>$zname1<>$zname2<>$zbong1<>$zbong2<>$zbong3<>\n");
	open(OUT,">$TOWN_LIST") or &ERR('TOWN �����͸� ������ �� �����ϴ�.');
	print OUT @TOWN_DATA;
	close(OUT);
	}
	}
	$num1++;
	}

	&HEADER;
	print <<"EOM";
<CENTER><hr size=0><h2>���並 �����߽��ϴ�.</h2><p>
<form action="./bong.cgi" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=BONG>
<input type=hidden name=num value=$in{'numd'}>
<input type=submit value="Ȯ��"></form></CENTER>

EOM

	&FOOTER;
	exit;

}
