sub GET_MONEY {

	if($in{'no'} eq ""){&ERR("NO:�� �Էµ��� �ʾҽ��ϴ�.");}
	&CHARA_MAIN_OPEN;
	&TOWN_DATA_OPEN("$kpos");
	&COUNTRY_DATA_OPEN("$kcon");

	$dir="./charalog/main";
	opendir(dirlist,"$dir");
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i){
			if(!open(page,"$dir/$file")){
				&ERR("���� ���� ����!");
			}
			@page = <page>;
			close(page);
			push(@CL_DATA,"@page<br>");
		}
	}
	closedir(dirlist);

	@tmp = map {(split /<>/)[10]} @CL_DATA;
	@CL_DATA = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];
	foreach(@no){
		$no_list .= "<input type=hidden name=no value=$_>"
	}

	&HEADER;
	$no = $in{'no'} + 1;

	$get_sol = $klea - $ksol;
	print <<"EOM";
<TABLE border=0 width=100% height=80%><TR><TD align=center>
<TABLE border=0 width=100%>
<TR><TH>
<img src="$img/sam/image/b8.gif">
</TH></TR>
<TR><TD>
<center><TABLE bgcolor=$ELE_BG[$xele]><TBODY bgcolor=$ELE_C[$xele]>
<TR><TH colspan=7 bgcolor=$ELE_BG[$xele]><font color=$ELE_C[$xele]>$kname</font></TH></TR>

<TR><TD rowspan=2 width=5><img src=$IMG/sam/image/$kchara.gif></TD><TD>����</TD><TH>$kstr</TH><TD>����</TD><TH>$kint</TH><TD>��ַ�</TD><TH>$klea</TH></TR>
<TR><TD>��</TD><TH>$kgold</TH><TD>��</TD><TH>$krice</TH><TD>����</TD><TH>$kcex</TH></TR>
<TR><TD>�Ҽӱ�</TD><TH colspan=2>$cou_name[$kcon]��</TH><TD>����</TD><TH>$ksol</TH><TD>�Ʒ�</TD><TH>$kgat</TH></TR>
</TBODY></TABLE>
</TD></TR>
<TR><TD>
<TABEL bgcolor=#AA0000><TR><TD bgcolor=#000000>
<center><font color=white>�ٸ� ������ ����� ����մϴ�.<BR>����ϴµ� �� 200-�ŷ�ġ�� �ʿ��մϴ�.<BR>(���� : �м��� ���ڼ��� ���� 60���� �̳��� �ۼ��Ͻʽÿ�.)</font>
</TD></TR></TABLE>
</TD></TR>
<TR><TD>
<center><form action="$COMMAND" method="POST"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<p>[����ϴ� ��븦 ����]<BR><select name=num>
<option value="">����Ϸ��� ����� �������ֽʽÿ�.
EOM

	foreach(@COU_DATA){
		($xccid,$xcname,$xcele,$xcmark,$xcking,$xcmes,$xcsub,$xcpri)=split(/<>/);
		$cou_king[$xccid] = "$xcking";
	}

	$con_l2 = "<option value=>================================= ����λ� =================================\n";
	foreach(@CL_DATA) {
		($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos) = split(/<>/);
		if($eid eq $kid) { next; }
		if($econ eq $kcon) { next; }
		if($cou_name[$econ] eq ""){
			$con_l2 .= "<option value=$eid>���̸�:$ename�� ������:$estr�� ������:$eint�� ����ַ�:$elea�� ���ŷ�:$echa�� ���漺��:$ebank��\n";
			next;
		}
		if($wcon ne $econ){
			$con_l .= "<option value=>================================= $cou_name[$econ]�� =================================\n";
		}
		$wcon = $econ;
		if($cou_king[$econ] eq $eid){next;}
		$con_l .= "<option value=$eid>���̸�:$ename�� ������:$estr�� ������:$eint�� ����ַ�:$elea�� ���ŷ�:$echa�� ���漺��:$ebank��\n";
	}

print <<"EOM";
$con_l
$con_l2
</select>

$no_list
<BR><br><font color=red>[��뿡�� ������ ��������]</font><BR>
<textarea name=mes cols=38 rows=3>
</TEXTAREA>
<center><br><input type=hidden name=mode value=33>
<input type=submit value="����Ѵ�"></form>


<center><form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="���ƿ´�"></form></CENTER>
</TD></TR></TABLE>
</TD></TR></TABLE>

EOM

	&FOOTER;

	exit;

}
1;