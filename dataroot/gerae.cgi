
sub GERAE{
						$ksub2=0;

						if($zsouba){
							if($kskill =~ /Ab/){
							if($cnum > 5000){
								$cnum = 5000;
							}
							}else{
							if($cnum > 3000){
							$cnum = 3000;
							}
							}

							if($kcodea =~ /C7/ && 30 > rand(100)){
								if($kchat > rand(200)){
								$kqpoint += 1;
								&K_LOG("$mmonth�� : [����] �̰� ����? ������? ó����� ���ε�? �ѹ� �Ծ��?");
								&K_LOG("$mmonth�� : �����밡 ���ε� ���̿��� ���� ����� ���� ����̴�.");
								}else{
								&K_LOG("$mmonth�� : [����] ���� ����ϴ��� �ٻڴϱ� �̷� �������� �� �Ȱ��������� ���ڳ�.");
								}
							}

							if(!$cno){
								if($kgold >= $cnum){
									if($cnum * $zsouba){
										if($kskill =~ /Bb/){
										$kadd = int(((2-$zsouba) * $cnum)*1.5);
										}else{
										$kadd = int((2-$zsouba) * $cnum);
										}
									}else{
										$kadd = 0;
									}
									$kgold -= $cnum;
									$krice += $kadd;
									&K_LOG("$mmonth�� : [����] : �� $cnum�� ������ $kadd�� ���� ����ϴ�.");
									$kint_ex++;
									$go_ex += int($kbank/5);
									$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,$bo_ex,$gi_ex,$ch_ex,$gu_ex,$go_ex,$jin_ex,";
								}else{
									&K_LOG("$mmonth�� : [����] : �������� ������� �ʽ��ϴ�.");
								}
							}else{
								if($krice > $cnum){
										if($kskill =~ /Bb/){
										$kadd = int(($cnum * $zsouba)*1.5);
										}else{
										$kadd = int($cnum * $zsouba);
										}
									$krice -= $cnum;
									$kgold += $kadd;
									&K_LOG("$mmonth�� : [����] : $cnum�� ���� �Ⱦ� $kadd�� ���� ����ϴ�.");
									$kint_ex++;
									$go_ex += int($kbank/5);
									$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,$bo_ex,$gi_ex,$ch_ex,$gu_ex,$go_ex,$jin_ex,";
								}else{
									&K_LOG("$mmonth�� : [����] : ���� ������� �ʽ��ϴ�.");
								}
							}
						}
}
1;

