#!/usr/bin/perl

require 'jcode.pl';
require './ini_file/index.ini';
require 'suport.cgi';

if($MENTE) { &ERR2("로딩중입니다. 잠깐 기다려 주세요."); }
&DECODE;
if($ENV{'HTTP_REFERER'} !~ /i/ && $CHEACKER){ &ERR2("주소 바에 값을 입력하지 말아주세요."); }
if($mode eq 'MES_SEND') { require 'mydata/mes_send.cgi';&MES_SEND; }
elsif($mode eq 'COUNTRY_TALK') { require 'mydata/country_talk.cgi';&COUNTRY_TALK; }
elsif($mode eq 'COUNTRY_WRITE') { require 'mydata/country_write.cgi';&COUNTRY_WRITE; }
elsif($mode eq 'COUNTRY_W') { require 'mydata/country_w.cgi';&COUNTRY_W; }
elsif($mode eq 'COUNTRY_W1') { require 'mydata/country_w1.cgi';&COUNTRY_W1; }
elsif($mode eq 'COUNTRY_TALK1') { require 'mydata/country_talk1.cgi';&COUNTRY_TALK1; }
elsif($mode eq 'COUNTRY_WRITE1') { require 'mydata/country_write1.cgi';&COUNTRY_WRITE1; }
elsif($mode eq 'COUNTRY_W2') { require 'mydata/country_w2.cgi';&COUNTRY_W2; }
elsif($mode eq 'COUNTRY_TALK2') { require 'mydata/country_talk2.cgi';&COUNTRY_TALK2; }
elsif($mode eq 'COUNTRY_WRITE2') { require 'mydata/country_write2.cgi';&COUNTRY_WRITE2; }
elsif($mode eq 'LOCAL_RULE') { require 'mydata/local_rule.cgi';&LOCAL_RULE; }
elsif($mode eq 'LOCAL_RULE1') { require 'mydata/local_rule1.cgi';&LOCAL_RULE1; }
elsif($mode eq 'L_RULE_WRITE') { require 'mydata/l_rule_write.cgi';&L_RULE_WRITE; }
elsif($mode eq 'L_RULE_DEL') { require 'mydata/l_rule_del.cgi';&L_RULE_DEL; }
elsif($mode eq 'JIN') { require 'mydata/jin.cgi';&JIN; }
elsif($mode eq 'JIN1') { require 'mydata/jin.cgi';&JIN1; }

elsif($mode eq 'BONGTOG') { require './bongtog.cgi';&BONGTOG; }
elsif($mode eq 'BONGTOG_W') {  require './bongtog_w.cgi';&BONGTOG_W;  }
elsif($mode eq 'BONGTOG_WRITE') {  require './bongtog_write.cgi';&BONGTOG_WRITE;  }
elsif($mode eq 'COU_CHANGE') { require 'mydata/cou_change.cgi';&COU_CHANGE; }
elsif($mode eq 'CYUUSEI') { require 'mydata/cyuusei.cgi';&CYUUSEI; }
elsif($mode eq 'LETTER') { require 'mydata/letter.cgi';&LETTER; }
elsif($mode eq 'KING_COM') { require 'mydata/king_com.cgi';&KING_COM; }
elsif($mode eq 'KING_COM2') { require 'mydata/king_com2.cgi';&KING_COM2; }
elsif($mode eq 'KING_COM3') { require 'mydata/king_com3.cgi';&KING_COM3; }
elsif($mode eq 'KING_COM4') { require 'mydata/king_com4.cgi';&KING_COM4; }
elsif($mode eq 'KING_COM5') { require 'mydata/king_com5.cgi';&KING_COM5; }
elsif($mode eq 'KING_COM6') { require 'mydata/king_com6.cgi';&KING_COM6; }
elsif($mode eq 'KING_COM7') { require 'mydata/king_com7.cgi';&KING_COM7; }

elsif($mode eq 'UNIT_ENTRY') { require 'mydata/unit_entry.cgi';&UNIT_ENTRY; }
elsif($mode eq 'UNIT_SELECT') { require 'mydata/unit_select.cgi';&UNIT_SELECT; }
elsif($mode eq 'UNIT_OUT') { require 'mydata/unit_out.cgi';&UNIT_OUT; }
elsif($mode eq 'MAKE_UNIT') { require 'mydata/make_unit.cgi';&MAKE_UNIT; }
elsif($mode eq 'UNIT_DELETE') { require 'mydata/unit_delete.cgi';&UNIT_DELETE; }
elsif($mode eq 'UNIT_CHANGE') { require 'mydata/unit_change.cgi';&UNIT_CHANGE; }
elsif($mode eq 'JIN') { require 'mydata/jin.cgi';&JIN; }

else{&ERR('올바르게 선택되지 않았습니다.');}

