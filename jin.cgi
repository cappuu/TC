#!/usr/bin/perl

require 'jcode.pl';
require './ini_file/index.ini';
require 'suport.cgi';

if($MENTE) { &ERR2("�ε����Դϴ�. ��ø� ��ٷ� �ֽʽÿ�"); }
&DECODE;

&INDEX;

sub INDEX {

	if ($in{'id'} =~ /[^0-9a-zA-Z]/){
		&ERR2("�����Դϴ�.");
	}



	open(IN,"./charalog/main/$in{'id'}.cgi") or &ERR2('ID�� �н��� �ùٸ��� �ʽ��ϴ�!');
	@CN_DATA = <IN>;
	close(IN);

	($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$kskill,$kpoint,$kct) = split(/<>/,$CN_DATA[0]);
	($kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex) = split(/,/,$ksub1);

	print <<"EOM";
	<form action="jin.cgi" method="post" name=para><input type="hidden" name="mode" value="JIN">
	<input type="radio" name="jin" value="1">����1<br>
	<input type="radio" name="jin" value="2">����2<br>
	<input type="radio" name="jin" value="3">����3<br>
	<input type="radio" name="jin" value="4">����4<br>
	<input type="radio" name="jin" value="5">����5<br>
	<input type="submit" style="font-family:�ü�; color:rgb(255,153,0); background-color:rgb(41,60,66); border-style:none;" value="��������"></form>
EOM

	&FOOTER;
	exit;
}

sub JIN {
	$dir="./charalog/main";
	opendir(dirlist,"$dir");
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i){
			if(!open(page,"$dir/$file")){
				&ERR2("���� ���� ����!");
			}
			@page = <page>;
			close(page);
			($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$kskill,$kpoint,$kct) = split(/<>/,$page[0]);
			$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,$kjin,";
			$kjin = $in{'jin'};
			&CHARA_MAIN_INPUT;
			}}
	closedir(dirlist);

	if($in{'jin'} eq 1){
	$jinb = '����1';
	}elsif($in{'jin'} eq 2){
	$jinb = '����2';
	}elsif($in{'jin'} eq 3){
	$jinb = '����3';
	}elsif($in{'jin'} eq 4){
	$jinb = '����4';
	}elsif($in{'jin'} eq 5){
	$jinb = '����5';
	}

	&HEADER;
	print <<"EOM";
<center><h2><font color=blue>$jinb�� ������ �����Ͽ����ϴ�.</font></h2><hr size=0>
<br>
<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="Ȯ��"></form>
EOM

	&FOOTER;
	exit;
}