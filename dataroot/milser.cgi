
sub MILSER{
						$ksub2=0;
						if($kgold < 100){
							&K_LOG("$mmonth�� : ���� ������� �ʽ��ϴ�.");
						}elsif($xmark < $BATTLE_STOP && $con_num >= $CON_ENTRY_MAX){
						&E_ERR("�� ����� ������ �ѱ�� �����Ƿ� �Ա��� ���� �����ϴ�.");
						}else{
							open(IN,"$QUEST_DATA");
							@QUEST_DATA = <IN>;
							close(IN);

							foreach(@QUEST_DATA){
							($qnum,$qcode,$qface,$qname,$qlevel,$quest,$qlimit,$qtalka,$qtalkb,$qtalkc,$qgold,$qrice,$qstr,$qint,$qlea,$qcha,$qcex,$qexp,$qseal,$qflag,$qcategory,$qrate,$qtalkd,$qup) = split(/<>/);
								if($kcodea =~ /$qcode/ && $qrate > rand(99)){
									if($qcategory =~ /�м�/){
										$kqpoint += $qup;
										if($qtalkd eq ""){
										}else{
										&K_LOG("$mmonth�� : $qtalkd");
										}
									}	
								}
							}


							$kgold-= int(200 - $cha);
							$kcex += 30;
							$kexp += 30;
							$kpoint += 10;
							open(IN,"$MESSAGE_LIST2");
							@MES_REG2 = <IN>;
							close(IN);
							$mes_num = @MES_REG2;
							if($mes_num > $MES_MAX) { pop(@MES_REG2); }
							unshift(@MES_REG2,"$cnum<>$kid<>$kpos<>$kname<>$csub<>$cno<>$ctime<>$kchara<>$cend<>\n");
							open(OUT,">$MESSAGE_LIST2");
							print OUT @MES_REG2;
							close(OUT);
							&K_LOG("$mmonth�� : $cno���� �м��� ���½��ϴ�.");
							&MAP_LOG("<img src=$IMG/j21.gif> $cno���� �������� �д��� ������ �ֽ��ϴ�.");
							$kcha_ex++;
							$go_ex += int($kbank/5);
							$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,$bo_ex,$gi_ex,$ch_ex,$gu_ex,$go_ex,$jin_ex,";
						}
}
1;

