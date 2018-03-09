sub BUY2 {

	if($in{'no'} eq ""){&ERR("NO:가 입력되지 않았습니다.");}
	if($in{'num'} eq "" || $in{'num'} eq "0"){&ERR("매매하는 값을 입력하지 않았습니다.");}
	if($in{'type'} eq ""){&ERR("매매가 입력되지 않았습니다.");}
	if($in{'num'} =~ m/[^0-9]/){&ERR("매매하는 숫자 외에 문자가 포함되어 있습니다."); }
	&CHARA_MAIN_OPEN;
	&TOWN_DATA_OPEN("$kpos");

	open(IN,"./charalog/command/$kid.cgi");
	@COM_DATA = <IN>;
	close(IN);

	$mes_num = @COM_DATA;

	if($mes_num > $MAX_COM) { pop(@COM_DATA); }

	$sou1 = int($zsouba*$in{'num'});
	$sou2 = int((2-$zsouba)*$in{'num'});
	$pnum = $in{'num'} + 0;
	if($in{'type'}){
		$title_name = "쌀을 $pnum 판다 [금 $sou1]";
	}else{
		$title_name = "금을 $pnum 판다 [쌀 $sou2]";
	}

	@NEW_COM_DATA=();$i=0;
	if($in{'no'} eq "all"){
		while(@NEW_COM_DATA < $MAX_COM){
			push(@NEW_COM_DATA,"$in{'mode'}<>$in{'type'}<>$title_name<>$tt<>$zsouba<>$in{'num'}<><>\n");
		}
		$no = $in{'no'};
	}else{
		foreach(@COM_DATA){
			($cid,$cno,$cname,$ctime,$csub,$cnum,$cend) = split(/<>/);
			$ahit=0;
			foreach(@no){
				if($i eq $_){
					$ahit=1;
					push(@NEW_COM_DATA,"$in{'mode'}<>$in{'type'}<>$title_name<>$tt<>$zsouba<>$in{'num'}<><>\n");
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
	open(OUT,">./charalog/command/$kid.cgi") or &ERR('파일을 열지 않았습니다.');
	print OUT @NEW_COM_DATA;
	close(OUT);

	&HEADER;

	print <<"EOM";
<CENTER><hr size=0><h2>NO:$no에 $title_name를 입력했습니다.</h2><p>
<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="확인"></form></CENTER>
EOM

	&FOOTER;

	exit;

}
1;