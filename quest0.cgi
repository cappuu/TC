#!/usr/bin/perl

require 'jcode.pl';
require './ini_file/index.ini';
require 'suport.cgi';

if($MENTE) { &ERR2("�ε����Դϴ�. ��� ��ٷ� �ּ���."); }
&DECODE;
if($ENV{'HTTP_REFERER'} !~ /i/ && $CHEACKER){ &ERR2("�ּ� �ٿ� ���� �Է����� �����ּ���."); }
if($mode eq 'QUEST2') { require './quest/quest2.cgi';&QUEST2; }
elsif($mode eq 'QUEST') { require './quest/quest.cgi';&QUEST; }
elsif($mode eq 'QUEST3') { require './quest/quest3.cgi';&QUEST3; }
elsif($mode eq 'QUEST4') { require './quest/quest4.cgi';&QUEST4; }
elsif($mode eq 'QUEST5') { require './quest/quest5.cgi';&QUEST5; }
else{&ERR('�ùٸ��� ���õ��� �ʾҽ��ϴ�.');}