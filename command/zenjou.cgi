sub ZENJOU {

	if($in{'no'} eq ""){&ERR("NO:�� �Էµ��� �ʾҽ��ϴ�.");}
	&CHARA_MAIN_OPEN;
	&TOWN_DATA_OPEN("$kpos");
	&COUNTRY_DATA_OPEN("$kcon");

	$dir="./charalog/main";
	opendir(dirlist,"$dir");
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i){
			if(!open(page,"$dir/$file")){
				&ERR("���� ���� ����");
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
<TABLE border=0 width=100%><TR><TD align=center>
<TABLE border=0 width=100%>
<TR><TH bgcolor=414141>
<font color=ffffff> - �� �� �� �� [����Ŀ�ǵ�] - </font>
</TH></TR>
<TR><TD>
<TABEL bgcolor=#AA0000><TR><TD bgcolor=#000000>
<font color=white>�ڱ��� ������� �������� �����մϴ�.</font>
</TD></TR></TABLE>
</TD></TR>
<TR><TD>
<form action="$COMMAND" method="POST"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<p>[�İ��ڸ� ����]<BR><select name=num>
EOM

	foreach(@COU_DATA){
		($xccid,$xcname,$xcele,$xcmark,$xcking,$xcmes,$xcsub,$xcpri)=split(/<>/);
		$cou_king[$xccid] = "$xcking";
	}

	foreach(@CL_DATA) {
		($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos) = split(/<>/);
		if($econ eq $kcon){
			$con_l .= "<option value=$eid>$ename\n";
			next;
		}
	}

print <<"EOM";
$con_l
</select>

$no_list
<input type=hidden name=mode value=47>
<input type=submit value=\"������ �����ش�\"></form>


<form action="$FILE_STATUS" method="post">
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

sub ZENJOU2 {


	$dir="./charalog/main";
	opendir(dirlist,"$dir");
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i){
			if(!open(page,"$dir/$file")){
				&ERR("���� ���� ����");
			}
			@page = <page>;
			close(page);
			push(@CL_DATA,"@page<br>");
		}
	}
	closedir(dirlist);

	if($in{'no'} eq ""){&ERR("NO:�� �Էµ��� �ʾҽ��ϴ�.");}


	&CHARA_MAIN_OPEN;
	&COUNTRY_DATA_OPEN($kcon);

	$num = $in{'num'};
	$hit=0;
	open(IN,"./charalog/main/$num\.cgi") or &ERR('�� ĳ���ʹ� ����� �� �����ϴ�.');
	@E_DATA = <IN>;
	close(IN);
	($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos) = split(/<>/,$E_DATA[0]);


	open(IN,"./charalog/command/$kid.cgi");
	@COM_DATA = <IN>;
	close(IN);

	$mes_num = @COM_DATA;

	if($mes_num > $MAX_COM) { pop(@COM_DATA); }

	@NEW_COM_DATA=();$i=0;
	if($in{'no'} eq "all"){
		while(@NEW_COM_DATA < $MAX_COM){
			push(@NEW_COM_DATA,"$in{'mode'}<>$ename<>$ename���� �������<>9999<><>$in{'num'}<>$kcon<>\n");
		}
		$no = $in{'no'};
	}else{
		foreach(@COM_DATA){
			($cid,$cno,$cname,$ctime,$csub,$cnum,$cend) = split(/<>/);
			$ahit=0;
			foreach(@no){
				if($i eq $_){
					$ahit=1;
					push(@NEW_COM_DATA,"$in{'mode'}<>$ename<>$ename���� �������<>9999<><>$in{'num'}<>$kcon<>\n");
					$lno = $_ + 1;
					$no .= "$lno,";
				}
			}
			if(!$ahit){
				push(@NEW_COM_DATA,"$_");
			}
			$i++;
		}
	}
	open(OUT,">./charalog/command/$kid.cgi") or &ERR('������ ���� �ʾҽ��ϴ�.');
	print OUT @NEW_COM_DATA;
	close(OUT);

	&HEADER;

	print <<"EOM";
<CENTER><hr size=0><h2>$ename���� ��������� �Է��߽��ϴ�.</h2><p>
<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="Ȯ��"></form></CENTER>
EOM

	&FOOTER;

	exit;

}
1;

1;
