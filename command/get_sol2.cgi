sub GET_SOL2 {

	if($in{'no'} eq ""){&ERR("NO:�� �Էµ��� �ʾҽ��ϴ�.");}
	if($in{'num'} eq ""){&ERR("¡���ϴ� �ο����� �Էµ��� �ʾҽ��ϴ�.");}
	if($in{'type'} eq ""){&ERR("¡���ϴ� ������ �Էµ��� �ʾҽ��ϴ�.");}
	if($in{'num'} =~ m/[^0-9]/){&ERR("¡���ϴ� �ο����� ���� �̿��� ���ڰ� ���ԵǾ� �ֽ��ϴ�."); }
	&CHARA_MAIN_OPEN;
	&TIME_DATA;

	open(IN,"./charalog/command/$kid.cgi");
	@COM_DATA = <IN>;
	close(IN);

	$mes_num = @COM_DATA;

	if($kcha > 75){
	$ga = int($kcha/5);
	}
	$ggyo = int($in{'num'} * ($SOL_PRICE[$in{'type'}] - $ga)/30);
	if($ggyo < 10){$ggyo=int(($cnum * 10)/30);}

	if($mes_num > $MAX_COM) { pop(@COM_DATA); }

	@NEW_COM_DATA=();$i=0;
	if($in{'no'} eq "all"){
		while(@NEW_COM_DATA < $MAX_COM){
			push(@NEW_COM_DATA,"10<><>$SOL_TYPE[$in{'type'}]¡��($in{'num'}�� �ݾ�:$ggyo)<>$tt<>$in{'type'}<>$in{'num'}<>$in{'gat'}<>\n");
		}
		$no = $in{'no'};
	}else{
		foreach(@COM_DATA){
			($cid,$cno,$cname,$ctime,$csub,$cnum,$cend) = split(/<>/);
			$ahit=0;
			foreach(@no){
				if($i eq $_){
					$ahit=1;
					push(@NEW_COM_DATA,"10<><>$SOL_TYPE[$in{'type'}]¡��($in{'num'}�� �ݾ�:$ggyo)<>$tt<>$in{'type'}<>$in{'num'}<>$in{'gat'}<>\n");
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
<CENTER><hr size=0><h2>NO:$no�� $mes$SOL_TYPE[$in{'type'}]($in{'num'}��) ¡���� �Է��߽��ϴ�. �ݾ�:$ggyo</h2><p>
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