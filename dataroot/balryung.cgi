
sub BALRYUNG{
						$ksub2=0;
						$uhit=0;
						foreach(@UNI_DATA){
							($unit_id,$uunit_name,$ucon,$ureader,$uid)=split(/<>/);
							if("$uid" eq "$kid" && $unit_id eq $kid){$uhit=1;last;}
						}
						if(!$uhit){
							&K_LOG("$mmonth�� : ����ۿ� ������ �� �����ϴ�.");
						}else{

							foreach(@UNI_DATA){
								($unit_id,$uunit_name,$ucon,$ureader,$uid)=split(/<>/);
								if($unit_id eq $kid && $uid ne $unit_id){
									open(IN,"./charalog/main/$uid\.cgi");
									@E_DATA = <IN>;
									close(IN);
									($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos,$eskill,$epoint,$ect,$elevel,$eexp,$ecodea,$ecodeb,$eqpoint) = split(/<>/,$E_DATA[0]);
									if($csub eq $ename){							
									$epos = $cnum;
									&E_LOG2("$mmonth�� : ������ ��ɿ� ���� $town_name[$cnum]������ �߷ɵǾ����ϴ�.");
									&ENEMY_INPUT;
									}
								}
							}
							$kcha_ex++;
							$go_ex += int($kbank/5);
							$kcex+=30;
							$kpoint += 10;
							$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,$bo_ex,$gi_ex,$ch_ex,$gu_ex,$go_ex,$jin_ex,";
							&K_LOG("$mmonth�� : $csub���� $town_name[$cnum]������ �߷ɺ��½��ϴ�.");
						}
}
1;

