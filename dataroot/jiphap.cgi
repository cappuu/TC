
sub JIPHAP{
						$ksub2=0;
						$uhit=0;
						$unit_num = 0;
						foreach(@UNI_DATA){
							($unit_id,$uunit_name,$ucon,$ureader,$uid)=split(/<>/);
							if("$uid" eq "$kid" && $unit_id eq $kid){$uhit=1;last;}
						}
						if(!$uhit){
							&K_LOG("$mmonth�� : ����ۿ� ������ �� �����ϴ�.");
						}elsif(0 >= $kgold){
							&K_LOG("$mmonth�� : ���� �����մϴ�.");
							$kgold = 0;
						}else{
							foreach(@UNI_DATA){
								($unit_id,$uunit_name,$ucon,$ureader,$uid)=split(/<>/);
								if($unit_id eq $kid && $uid ne $unit_id){
									open(IN,"./charalog/main/$uid\.cgi");
									@E_DATA = <IN>;
									close(IN);
									($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos,$eskill,$epoint,$ect,$elevel,$eexp,$ecodea,$ecodeb,$eqpoint) = split(/<>/,$E_DATA[0]);						
									($estr_ex,$eint_ex,$elea_ex,$echa_ex,$esub1_ex,$esub2_ex,$ebo_ex,$egi_ex,$ech_ex,$egu_ex,$ego_ex,$ejin_ex) = split(/,/,$esub1);
									if($esol <= 500){
										$ego_ex += int($ebank/5);
										$epos = $kpos;
										&E_LOG2("$mmonth�� : $uunit_name�δ�� ������ ��ɿ� ���� $town_name[$kpos]���� �����߽��ϴ�.");
										&ENEMY_INPUT;
										$unit_num++;
									}else{
										&E_LOG2("$mmonth�� : ������ ���ո���� ���������� ������ 500�� �̻��Դϴ�. ");
									}
								}
							}
	
							$kcha_ex++;
							$go_ex += int($kbank/5);
							$kgold-= 30*$unit_num;
							$kcex+= 4*$unit_num;
							$kexp+= 4*$unit_num;
							$kpoint+= 2*$unit_num;
							$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,$bo_ex,$gi_ex,$ch_ex,$gu_ex,$go_ex,$jin_ex,";
							&K_LOG("$mmonth�� : �δ������ $town_name[$kpos]�� ������׽��ϴ�.");
						}
					
}
1;

