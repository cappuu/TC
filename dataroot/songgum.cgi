
sub SONGGUM{
					if($kgold<0){
					&K_LOG("���� ������� �ʽ��ϴ�.");
					}else{
					$susu = int($csub*30/100);
					$susu1 = $csub-$susu;
					&K_LOG("$cno�Կ��� $susu1�� ���� �۱��߽��ϴ�. [������: $susu]");
					$kgold-=$csub;

							open(IN,"$QUEST_DATA");
							@QUEST_DATA = <IN>;
							close(IN);

							foreach(@QUEST_DATA){
							($qnum,$qcode,$qface,$qname,$qlevel,$quest,$qlimit,$qtalka,$qtalkb,$qtalkc,$qgold,$qrice,$qstr,$qint,$qlea,$qcha,$qcex,$qexp,$qseal,$qflag,$qcategory,$qrate,$qtalkd,$qup) = split(/<>/);
								if($kcodea =~ /$qcode/ && $qrate > rand(99)){
									if($qcategory =~ /�۱�/){
										if($qup =~ /�۱�/){
										$kqpoint += $susu1;
										}else{
										$kqpoint += $qup;
										}
										if($qtalkd eq ""){
										}else{
										&K_LOG("$mmonth�� : $qtalkd");
										}
									}
								}
							}

					$kcex += int($csub/250);
					$kexp += int($csub/250);
					$kpoint += int($csub/500);
					$go_ex += int($kbank/5);
					$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,$bo_ex,$gi_ex,$ch_ex,$gu_ex,$go_ex,$jin_ex,";
					open(IN,"./charalog/main/$cnum\.cgi");
					@E_DATA = <IN>;
					close(IN);
					($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos,$eskill,$epoint,$ect,$elevel,$eexp,$ecodea,$ecodeb,$eqpoint) = split(/<>/,$E_DATA[0]);
					$egold += $susu1;
					&E_LOG2("$kname�Կ��Լ� $susu1�� ���� �۱ݹ޾ҽ��ϴ�. [������: $susu]");
					&ENEMY_INPUT;

					}
}
1;
