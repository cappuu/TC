sub entry_can{
	&CHARA_MAIN_OPEN;
	&TOWN_DATA_OPEN("$kpos");
	&COUNTRY_DATA_OPEN("$kcon");
	&CHARA_ITEM_OPEN;
	&TIME_DATA;

	if(!$wday){&error("��ȸ �����Ͽ� ��� ������ �� �����ϴ�.");}
	
	open(IN,"./data/entry_list.cgi") or &ERR2("����� ����Ʈ�� ������ �ʽ��ϴ�.");
	@ENTRY_DATA = <IN>;
	close(IN);
	@N_ENTRY=();
	foreach(@ENTRY_DATA){
		($e_id,$e_name,$e_chara,$e_con,$e_cname,$e_cele,$e_point,$e_flg)=split(/<>/);
		if($e_id eq $kid){$ehit=1;}
		else{push(@N_ENTRY,"$_");}
	}
	if(!$ehit){&ERR2("��ϵǾ� ���� �ʽ��ϴ�.");}
	open(OUT,">./data/entry_list.cgi");
	print OUT @N_ENTRY;
	close(OUT);

	&HEADER;
	
	print <<"EOF";
<TABLE border="0" width="80%" bgcolor="#ffffff" height="150" align=center CLASS=FC>
  <TBODY>
    <TR>
      <TD colspan="2" align="center" bgcolor="#993300"><FONT color="#ffffcc">��� ����</FONT></TD>
    </TR>
    <TR>
      <TD bgcolor="#ffffcc" width=20% align=center><img src="./img/etc/arena.jpg"></TD>
      <TD bgcolor="#330000"><FONT color="#ffffcc">����� �����߽��ϴ�.</FONT></TD>
    </TR>
    <TR>
      <TD colspan="2" align="right">
<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="���ƿ´�"></form></TD>
	
    </TR>
  </TBODY>
</TABLE>
EOF
	&footer;
	exit;
}
1;
