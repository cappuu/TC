#!/usr/bin/perl

require 'jcode.pl';
require './ini_file/index.ini';
require 'suport.cgi';

if($mode eq 'C_RAN') { &C_RAN; }
if($MENTE) { &ERR2("�ε����Դϴ�. ��ø� ��ٷ��ּ���."); }
&DECODE;

if($mode eq "") {require 'entry/entry.cgi'; &ENTRY; }
elsif($mode eq 'NEW_CHARA') { require 'entry/new_chara.cgi';require 'entry/data_send.cgi';&NEW_CHARA; }
elsif($mode eq 'DATA_SEND') { require 'entry/data_send.cgi';&DATA_SEND; }
elsif($mode eq 'RESISDENTS') { require 'entry/resisdents.cgi';&RESISDENTS; }
elsif($mode eq 'ATTESTATION') { require 'entry/attestation.cgi';&ATTESTATION; }
elsif($mode eq 'SET_ENTRY') { require 'entry/attestation.cgi';&SET_ENTRY; }
else{require 'entry/entry.cgi';&ENTRY;}

