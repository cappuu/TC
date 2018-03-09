sub COUNTRY_TALK1 {

	&CHARA_MAIN_OPEN;
	&COUNTRY_DATA_OPEN("$kcon");
    if($xcid eq 0){&ERR("재야인사는 사용할 수 없습니다.");}
	$sno = $kclass / 500;
	if($sno > 43){$sno = 43;}

	open(IN,"$BBS_LIST1") or &ERR('파일을 열지 않았습니다. err no :country_bbs');
	@BBS_DATA1 = <IN>;
	close(IN);


	&HEADER;

	print <<"EOM";

<table align="center" width="950">
    <tr>
        <td>
            <img src="$IMG/up.gif">
        </td>
    </tr>
    <tr>
        <td background="$IMG/backg.gif">
<TABLE WIDTH="100%" height=100%>
<TBODY><TR BGCOLOR=$ELE_BG[$xele]>
<STYLE>BODY {
	CURSOR: url('samnet.cur')
}
A {
	CURSOR: url('samnet.ani'); TEXT-DECORATION: none
}
</STYLE>
<TD WIDTH=100% height=5><font color=$ELE_C[$xele] size=4><center>-<B> 외교게시판 </B>-</font></TR></TD>
</TR><TR>
<TD height=5>
<TABLE border="0"><TBODY>
<TR>
<TD></TD>
<TD WIDTH=100% align=center>
<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit style="font-family:궁서; color:$ELE_C[$xele]; background-color:$ELE_BG[$xele]; border-width:1; border-color:black; border-style:solid;" value="메뉴로 돌아온다"></form>
<form action="./mydata.cgi" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=COUNTRY_W1>
<input type=submit style="font-family:궁서; color:$ELE_C[$xele]; background-color:$ELE_BG[$xele]; border-width:1; border-color:black; border-style:solid;" value="글쓰기"></form>
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
	$BBS_NEXT_NUM = 20;

	if($in{'bbs_no'} eq ""){
		$bbs_no = 0;
	}else{
		$bbs_no = $in{'bbs_no'};
	}

	$s_n = 0;
	$n = 0;
	foreach(@BBS_DATA1){
		($bbid,$bbtitle,$bbmes,$bbcharaimg,$bbname,$bbhost,$bbtime,$bbele,$bbcon,$bbtype,$bbno,$bbheap)=split(/<>/);
		if($bbtype eq "0"){
			if(!$bbheap){
				if($s_n >= $bbs_no && $s_n < $bbs_no + $BBS_NEXT_NUM){
				$bno = $s_n+1;
				$bb_id[$n] = $bbno;
				$n++;
				$c_mes[$bbno] = "<TABLE border=0 width=85% bgcolor=$ELE_C[$bbele]>

  <TBODY>
    <TR>
      <TD colspan=2 bgcolor=000000><B><font size=3 color=FFFFFF>제목 : $bbtitle</font></B></TD>
    </TR>
    <TR>
      <TD width=80 rowspan=3 valign=up align=center><img src=$IMG/$bbcharaimg.gif></TD>
      <TD>
      <TABLE border=0 width=100% bgcolor=$ELE_C[$bbele]>
        <TBODY>
          <TR>
            <TD width=600 bgcolor=$ELE_BG[$bbele]><font color=ffffff>$bbmes</TD>
          </TR>
        </TBODY>
      </TABLE>
      </TD>
    </TR>
    <TR>
      <TD><color=$ELE_BG[$bbele]><a href=\"javascript:info('$bbid')\">$bbname</a> </font></TD>
    </TR>
    <TR>
      <TD colspan=2 align=right><color=$ELE_BG[$bbele]>$bbtime</font></TD>
    </TR>

    <TR>
      <TD colspan=2 align=right>
<form action=\"./mydata.cgi\" method=\"post\">
<input type=text name=ins size=65>
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=b_no value=$bbno>
<input type=hidden name=mode value=COUNTRY_WRITE1>
<input type=submit value=답신>
</TD></TR></form>";
				}
			$s_n++;
			}
		}
	}

	foreach(@BBS_DATA1){
		($bbid,$bbtitle,$bbmes,$bbcharaimg,$bbname,$bbhost,$bbtime,$bbele,$bbcon,$bbtype,$bbno,$bbheap)=split(/<>/);
		if($kcon eq "$bbcon" && $bbtype eq "0"){
			if($bbheap){
				$l=0;
				foreach(@bb_id){
					if($bbheap eq $bb_id[$l]){
					$c_mes[$bbheap] .= "<TR><TD colspan=2 width=100%><TABLE cellspacing=1 width=100% bgcolor=$ELE_BG[$bbele]><TBODY bgcolor=$ELE_C[$bbele]><TR><TD width=100%><font color=$ELE_BG[$bbele]>$bbmes</TD><TD bgcolor=$ELE_BG[$bbele]><img src=$IMG/$bbcharaimg.gif></TD></TR><TR><TD colspan=2><font size=1 color=$ELE_BG[$bbele]><a href=\"javascript:info('$bbid')\">$bbname</a> <small>\[$bbtime\]</small></TD></TR></TABLE></TD></TR>";
					}
					$l++;
				}
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
<input type=hidden name=mode value=COUNTRY_TALK1>
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
EOM

	&FOOTER;
	exit;
}
1;