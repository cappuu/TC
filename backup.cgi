#!/usr/bin/perl

require 'jcode.pl';
require './ini_file/index.ini';
require 'suport.cgi';

if($MENTE) { &ERR("�ε����Դϴ�. ��ø� ��ٷ� �ֽʽÿ�."); }
&DECODE;
&BAK;


sub BAK {

	&CHARA_MAIN_OPEN;


	open(IN,"./charalog/bak/$in{'id'}.cgi");
	@KK = <IN>;
	close(IN);

	unshift(@KK,"$kid<>$kpass<>$kname<>$kchara<>$kstr<>$kint<>$klea<>$kcha<>$ksol<>$kgat<>$kcon<>$kgold<>$krice<>$kcex<>$kclass<>$karm<>$kbook<>$kbank<>$ksub1<>$ksub2<>$kpos<>$kmes<>$khost<>$kdate<>$kmail<>$kos<>$kskill<>$kpoint<>$kct<>$klevel<>$kexp<>$kcodea<>$kcodeb<>$kqpoint<>\n");

	open(OUT,">./charalog/bak/$in{'id'}.cgi");
	print OUT @KK;
	close(OUT);


	&HEADER;
	print <<"EOM";
<CENTER><hr size=0><h2>$in{'id'}���� �����͸� ����߽��ϴ�.</h2><p>
<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="Ȯ��"></form></CENTER>

EOM

	&FOOTER;
	exit;

}