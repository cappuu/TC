
sub YOGEAK{
	$def_num=1;
	$def_num1=0;
	foreach(@DEF_DATA){
		($did,$dname,$dtown_id,$dtown_flg,$dcon,$dchara,$dsol,$dsub1_ex,$dtown_battle,$ddef)=split(/<>/);
		if($kpos eq "$dtown_id"){
			$def_num++;
		}
		if($kid eq "$did" && $kpos eq "$dtown_id"){
			$def_num1 = 1;
		}
	}


						$ksub2=0;
						($zname,$zcon,$znum,$znou,$zsyo,$zshiro,$znou_max,$zsyo_max,$zshiro_max,$zpri,$zx,$zy,$zsouba,$zdef_att,$zsub1,$zsub2,$z[0],$z[1],$z[2],$z[3],$z[4],$z[5],$z[6],$z[7],$zname1,$zname2,$zbong1,$zbong2,$zbong3)=split(/<>/,$TOWN_DATA[$kpos]);
						if($zdef_att< 200){
						$def_nums = 3;
						}
						if($zdef_att<400){
						if($zdef_att>=200){
						$def_nums = 4;}
						}
						if($zdef_att<600){
						if($zdef_att>=400){
						$def_nums = 5;}
						}
						if($zdef_att<800){
						if($zdef_att>=600){
						$def_nums = 6;}
						}
						if($zdef_att<1001){
						if($zdef_att>=800){
						$def_nums = 7;}
						}

						if($ksol eq "0" || $ksol eq ""){
							&K_LOG("$mmonth�� : ���簡 ���� ����� �� �� �����ϴ�..");
						}elsif($ksol < 499){
							&K_LOG("$mmonth�� : ����� ���ؼ� �ּ� 500�� �̻��� ������ �ʿ��մϴ�.");
						}elsif($def_num1){
							&K_LOG("$mmonth�� : �̹� �ش� ���ÿ� ����� �ɷ��ִ� �����Դϴ�.");
						}elsif($def_num >= $def_nums){
							&K_LOG("$mmonth�� : ����ο��� ���� á���ϴ�.");
						}elsif($kgat < 49){
							&K_LOG("$mmonth�� : ����� ���ؼ� �ּ� �Ʒõ��� 50�̻��� �Ǿ�� �մϴ�.");
						}else{

							open(IN,"$QUEST_DATA");
							@QUEST_DATA = <IN>;
							close(IN);

							foreach(@QUEST_DATA){
							($qnum,$qcode,$qface,$qname,$qlevel,$quest,$qlimit,$qtalka,$qtalkb,$qtalkc,$qgold,$qrice,$qstr,$qint,$qlea,$qcha,$qcex,$qexp,$qseal,$qflag,$qcategory,$qrate,$qtalkd,$qup) = split(/<>/);
								if($kcodea =~ /$qcode/ && $qrate > rand(99)){
									if($qcategory =~ /���/){
										$kqpoint += $qup;
										if($qtalkd eq ""){
										}else{
										&K_LOG("$mmonth�� : $qtalkd");
										}
									}	
								}
							}



							$kqpoint += 1 if $ksol >= 2000 && $kcodea =~ /C4/;
							open(IN,"$DEF_LIST");
							@DEF_LIST = <IN>;
							close(IN);
							my @NEW_DEF_LIST2=();
							$whit=0;
							foreach(@DEF_LIST){
								($tid,$tname,$ttown_id,$ttown_flg,$tcon,$tchara,$tsol,$tsub1_ex,$ttown_battle,$tdef) = split(/<>/);
								if("$tid" eq "$kid"){
								}else{
									push(@NEW_DEF_LIST2,"$_");
								}
							}
							unshift(@NEW_DEF_LIST2,"$kid<>$kname<>$kpos<>0<>$kcon<>$kchara<>$ksol<>$ksub1_ex<>0<>0<>\n");
							open(OUT,">$DEF_LIST");
							print OUT @NEW_DEF_LIST2;
							close(OUT);
							$kcex += 25;
							$kexp += 25;
							$kpoint += 8;
							&K_LOG("$mmonth�� : $zname������ ����� �Ϸ�Ǿ����ϴ�. $kstrt");
							&MAP_LOG("<img src=$IMG/j20.gif> $kname���� $zname���� ����� �غ��ϰ� �ֽ��ϴ�.");
							$klea_ex++;
							$go_ex += int($kbank/5);
							$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,$bo_ex,$gi_ex,$ch_ex,$gu_ex,$go_ex,$jin_ex,";
						}
}
1;

