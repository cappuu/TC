
sub SANGUP{
						$ksub2=0;
						if($kgold<50){
							&K_LOG("$mmonth�� : �ڱݺ������� ������ �� �������ϴ�.");
						}elsif($zsyo >= $zsyo_max){
							&K_LOG("$mmonth�� : ���ġ�� �ְ��Դϴ�.");
							$zsyo = $zsyo_max;						
							}else{
							if($kskill =~ /Ba/){
							$zsyoadd = int(int($kintt)/8 + rand($kintt) / 15);
							}else{
							$zsyoadd = int(int($kintt)/12 + rand($kintt) / 20);
							}

							$zsyo += $zsyoadd;
							$kgold -= 50;
							if($zsyo > $zsyo_max){
								$zsyo = $zsyo_max;
							}

							open(IN,"$QUEST_DATA");
							@QUEST_DATA = <IN>;
							close(IN);

							foreach(@QUEST_DATA){
							($qnum,$qcode,$qface,$qname,$qlevel,$quest,$qlimit,$qtalka,$qtalkb,$qtalkc,$qgold,$qrice,$qstr,$qint,$qlea,$qcha,$qcex,$qexp,$qseal,$qflag,$qcategory,$qrate,$qtalkd,$qup) = split(/<>/);
								if($kcodea =~ /$qcode/ && $qrate > rand(99)){
									if($qcategory =~ /���/){
										if($qup =~ /���/){
										$kqpoint += $zsyoadd;
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

							if($kcodea =~ /B1/ && 15 > rand(100)){
								$kqpoint += 1;
								&K_LOG("$mmonth�� : [������]: ����, �� ����� �����̰� ���´ٰ�? �� ���ڴٰ� �����ְԳ�.��");
							}

							if($kcodea =~ /B3/ && 6 > rand(100)){
								if($kstrt > rand(100)){
								$kqpoint += 1;
								&K_LOG("$mmonth�� : [������]: ����, �հ����� ����� ����߱�. �������ȴ�! �����!��");
								}else{
								&K_LOG("$mmonth�� : [������]: �������� ���� �̱���� �鸸���� �־��ٱ�!��");
								}
							}

							if($kcodea =~ /A3|C3/){
							$kqpoint += $zsyoadd;
							}

							$kcex += 30;
							$kexp += 30;
							$kpoint += 10;
							if("$zname" ne ""){
								splice(@TOWN_DATA,$kpos,1,"$zname<>$zcon<>$znum<>$znou<>$zsyo<>$zshiro<>$znou_max<>$zsyo_max<>$zshiro_max<>$zpri<>$zx<>$zy<>$zsouba<>$zdef_att<>$zsub1<>$zsub2<>$z[0]<>$z[1]<>$z[2]<>$z[3]<>$z[4]<>$z[5]<>$z[6]<>$z[7]<>$zname1<>$zname2<>$zbong1<>$zbong2<>$zbong3<>\n");
							}
							&K_LOG("$mmonth�� : $zname�� ����� <font color=red>+$zsyoadd</font> �������׽��ϴ�.");
							$kint_ex++;
							$go_ex += int($kbank/5);
							$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,$bo_ex,$gi_ex,$ch_ex,$gu_ex,$go_ex,$jin_ex,";
						}
}
1;

