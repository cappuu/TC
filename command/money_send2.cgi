sub MONEY_SEND2 {

	if($in{'no'} eq ""){&ERR("NO:�� �Էµ��� �ʾҽ��ϴ�.");}
	if($in{'num'} eq ""){&ERR("��밡 �Է����� �ʰ� �ֽ��ϴ�.");}

	&CHARA_MAIN_OPEN;
	&COUNTRY_DATA_OPEN($kcon);
	if($kgold < $in{'gold'}){&ERR("�۱��Ҹ��� ���� �����ϴ�.");}
	if($in{'gold'} =~ m/[^0-9]/){&ERR("�ݾ׿� ���� �̿��� ���ڰ� ���ԵǾ� �ֽ��ϴ�.");}

	if($kskill =~ /Ab/){
	if($in{'gold'} > 10001){&ERR("�۱� �ѵ����� �� 10000�Դϴ�.");}
	}else{
	if($in{'gold'} > 5001){&ERR("�۱� �ѵ����� �� 5000�Դϴ�.");}
	}

	$num = $in{'num'};
	$hit=0;

	open(IN,"./charalog/main/$num\.cgi") or &ERR('�� ĳ���Ϳ��� �۱��� �� �����ϴ�..');
	@E_DATA = <IN>;
	close(IN);
	($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos,$epoint,$ect,$elevel,$eexp,$ecodea,$ecodeb,$eqpoint) = split(/<>/,$E_DATA[0]);


	open(IN,"./charalog/command/$kid.cgi");
	@COM_DATA = <IN>;
	close(IN);

	$mes_num = @COM_DATA;

	if($mes_num > $MAX_COM) { pop(@COM_DATA); }

	@NEW_COM_DATA=();$i=0;
	if($in{'no'} eq "all"){
		while(@NEW_COM_DATA < $MAX_COM){
				push(@NEW_COM_DATA,"$in{'mode'}<>$ename<>$ename���� �� $in{'gold'}�� �۱�<>9999<>$in{'gold'}<>$in{'num'}<>$kcon<>\n");
		}
		$no = $in{'no'};
	}else{
		foreach(@COM_DATA){
			($cid,$cno,$cname,$ctime,$csub,$cnum,$cend) = split(/<>/);
			$ahit=0;
			foreach(@no){
				if($i eq $_){
					$ahit=1;
					push(@NEW_COM_DATA,"$in{'mode'}<>$ename<>$ename���� �� $in{'gold'}�� �۱�<>9999<>$in{'gold'}<>$in{'num'}<>$kcon<>\n");
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
<CENTER><hr size=0><h2>NO:$no�� $ename���� �� $in{'gold'} �۱��� �Է��߽��ϴ�.</h2><p>
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