
sub COUNTRY_TALK2 {

	&CHARA_MAIN_OPEN;
	&COUNTRY_DATA_OPEN("$kcon");
	$sno = $kclass / 500;
	if($sno > 43){$sno = 43;}

	open(IN,"$BBS_LIST2") or &ERR('파일을 열지 않았습니다. err no :country_bbs');
	@BBS_DATA = <IN>;
	close(IN);

	open(IN,"$COUNTRY_MES") or &ERR("지정된 파일이 열리지 않습니다.");
	@MES_DATA = <IN>;
	close(IN);

	$mess .= "<TR><TD colspan=2><center><img src=$IMG/gonggo.gif></TD></TR>";
	foreach(@MES_DATA){
		($cmes,$cid)=split(/<>/);
		$mess .= "<TR><TD bgcolor=$ELE_C[$cou_ele[$cid]] width=10%><center>$cou_name[$cid]</TD><TD bgcolor=$ELE_C[$cou_ele[$cid]] width=90%>$cmes</TD></TR>";
	}


	&HEADER;

	print <<"EOM";
<body leftmargin="0" marginwidth="0" topmargin="0" marginheight="0">
<table align="center" width="950">
    <tr>
        <td height="93">
            <img src="$IMG/up.gif">
        </td>
    </tr>
    <tr>
        <td background="$IMG/backg.gif">
<TABLE WIDTH="100%" height=100%>
<TBODY><TR>
<STYLE>BODY {
	CURSOR: url('samnet.cur')
}
A {
	CURSOR: url('samnet.ani'); TEXT-DECORATION: none
}
</STYLE>
<TD>
<table align="center" width=80%>
$mess
</table>
</TD>
</TR><TR>
<TD height=5>
<TABLE border="0"><TBODY>
<TR>
<TD></TD>
<TD WIDTH=100% align=center>
<table>
    <tr>
        <td>
<form action="./mydata.cgi" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=COUNTRY_W2>
<input type=submit style="font-family:궁서; color:$ELE_C[$xele]; background-color:#55240B; border-width:1; border-color:black; border-style:solid;" value="게시판에 글을 쓴다"></form>

        </td>
        <td>
<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit style="font-family:궁서; color:$ELE_C[$xele]; background-color:#55240B; border-width:1; border-color:black; border-style:solid;" value="메뉴로 돌아온다"></form>
        </td>
    </tr>
</table>
</TD>
</TR>
</TBODY></TABLE>
</TD>
</TR>
<TR>
<TD align=center>

<br>
</font>
EOM
	$BBS_NEXT_NUM = 5;

	if($in{'bbs_no'} eq ""){
		$bbs_no = 0;
	}else{
		$bbs_no = $in{'bbs_no'};
	}

	$s_n = 0;
	$n = 0;
	foreach(@BBS_DATA){
		($bbid,$bbtitle,$bbmes,$bbcharaimg,$bbname,$bbhost,$bbtime,$bbele,$bbcon,$bbtype,$bbno,$bbheap)=split(/<>/);
			if(!$bbheap){
				if($s_n >= $bbs_no && $s_n < $bbs_no + $BBS_NEXT_NUM){
				$bno = $s_n+1;
				$bb_id[$n] = $bbno;
				$n++;
				$c_mes[$bbno] = "<TABLE border=0 width=85% bgcolor=#990000>

  <TBODY>
    <TR>
      <TD colspan=3 bgcolor=#55240B><B><font size=3 color=$ELE_C[$bbele]>제목 : $bbtitle</font></B></TD>
    </TR>
    <TR>
      <TD width=80 rowspan=3 valign=up align=center><img src=$IMG/$bbcharaimg.gif>
</TD>
      <TD colspan=2>
      <TABLE border=0 width=100% bgcolor=$ELE_C[$bbele]>
        <TBODY>
          <TR>
            <TD width=600 bgcolor=#55240B><font color=ffffff>$bbmes</TD>
          </TR>
        </TBODY>
      </TABLE>
      </TD>
    </TR>

    <TR>
      <TD rowspan=2>
<IFRAME  FRAMEBORDER=no SCROLLING=no WIDTH=34 HEIGHT=44 SRC='../sam/avatar.cgi?id=$bbid'>
</TD>
</IFRAME>
     <TD width=1000><color=$ELE_BG[$bbele]><a href=\"javascript:info('$bbid')\">$bbname</a> </font></TD>
        <td></td>
    </TR>
    <TR>
      <TD colspan=2><color=$ELE_BG[$bbele]>$bbtime</font></TD>
    </TR>

    <TR>
      <TD colspan=3 align=right>
<form action=\"./mydata.cgi\" method=\"post\">
<input type=text name=ins size=65 style=font-family:궁서; color:#55240B; background-color:$ELE_BG[$xele];>
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=b_no value=$bbno>
<input type=hidden name=mode value=COUNTRY_WRITE2>
<input type=submit value=답신>
</TD></TR></form>";
				}
			$s_n++;
		}
	}

	foreach(@BBS_DATA){
		($bbid,$bbtitle,$bbmes,$bbcharaimg,$bbname,$bbhost,$bbtime,$bbele,$bbcon,$bbtype,$bbno,$bbheap)=split(/<>/);
			if($bbheap){
				$l=0;
				foreach(@bb_id){
					if($bbheap eq $bb_id[$l]){
					$c_mes[$bbheap] .= "<TR><TD colspan=3 width=100%><TABLE cellspacing=1 width=100% bgcolor=#55240B><TBODY bgcolor=$ELE_C[$bbele]><TR><TD width=100%><font color=$ELE_BG[$bbele]>$bbmes</font></TD><TD bgcolor=$ELE_BG[$bbele]><img src=$IMG/$bbcharaimg.gif></TD></TR><TR><TD><font size=1 color=$ELE_BG[$bbele]><a href=\'javascript:info('$bbid')\'>$bbname</a> <small>\[$bbtime\]</font></small></TD><TD align=center><IFRAME WIDTH=34 HEIGHT=44 FRAMEBORDER=no SCROLLING=no SRC='../sam/avatar.cgi?id=$bbid' MARGINWIDTH=0 MARGINHEIGHT=0 NAME=avatar HSPACE=0 VSPACE=0></IFRAME></TD></TR></TABLE></TD></TR>";
					}
					$l++;
				}
			}
	}

	$s=@c_mes;
	$d=0;
	foreach(@c_mes){
		$new_c_mes[$s] = $c_mes[$d];
		$s--;
		$d++;
	}

	foreach(@new_c_mes){
		if($_ ne ""){
			print "$_ </TBODY></TABLE><p>";
		}
	}

	$q=0;
	$n_bbs = $bbs_no + $BBS_NEXT_NUM;
	if($s_n >= $n_bbs){
	print " <form action=\"./mydata.cgi\" method=\"post\">
<input type=hidden name=mode value=COUNTRY_TALK2>
<input type=hidden name=bbs_no value=$n_bbs>
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=submit value=\"다음의 $BBS_NEXT_NUM건\">
</form>";
	}
print <<"EOM";
</CENTER>
</TD>
</TR>
</TBODY></TABLE>
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
1;