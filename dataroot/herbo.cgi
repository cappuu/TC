
sub HERBO{
				$ksub2=0;
				if($kgold<100){
					&K_LOG("$mmonth�� : �ڱݺ������� ������ �� �������ϴ�.");
				}else{
						open(IN,"$TRAP_LIST");
						@TRAP_DATA = <IN>;
						close(IN);
					$kgold -= 100;
					$trap_count = 0;
					$trap_flg = 0;
					$trapmax = @TRAP_DATA;
					if($kskill =~ /Dc/){
					$r = int(rand($kchat) + rand($kchat));
					}else{
					$r = int((rand($kchat) + rand($kchat))/2);
					}
					for($trapi=0;$trapi<$trapmax;$trapi++){
						($tid,$tname,$ttown_id,$tcon,$ttrap,$tint) = split(/<>/,$TRAP_DATA[$trapi]);
						if( $ttown_id == $kpos && $ttrap == 3 && $tid eq $kid ){
							$r += 5;
							if($r > $tint){
								$trap_flg = 1;
							}else{
								$trap_flg = -1;
							}
							last;
						}elsif( $ttown_id == $kpos ){
							$trap_count++;
						}
					}
					if( $trap_flg == -1 ){
						&K_LOG("$mmonth�� : �㺸�� ������ �� �������ϴ�.");
					}elsif( $trap_flg == 1 ){
						splice(@TRAP_DATA,$trapi,1,"$kid<>$kname<>$kpos<>$kcon<>3<>$r<>\n");
					if($kskill =~ /Dc/){
						$kcex += 40;
						$kexp += 40;
						$kpoint += 16;
					}else{
						$kcex += 20;
						$kexp += 20;
						$kpoint += 8;
					}
						&K_LOG("$mmonth�� : $zname���� �㺸�� �����Ͽ����ϴ�.");
						$kcha_ex += 2;
						$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,$bo_ex,$gi_ex,$ch_ex,$gu_ex,$go_ex,$jin_ex,";
					}elsif( $trap_count < 5 ){
						push(@TRAP_DATA,"$kid<>$kname<>$kpos<>$kcon<>3<>$r<>\n");
					if($kskill =~ /Dc/){
						$kcex += 40;
						$kexp += 40;
						$kpoint += 16;
					}else{
						$kcex += 20;
						$kexp += 20;
						$kpoint += 8;
					}
						&K_LOG("$mmonth�� : $zname���� �㺸�� ��ġ�Ͽ����ϴ�.");
						$kcha_ex += 2;
						$go_ex += int($kbank/5);
						$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,$bo_ex,$gi_ex,$ch_ex,$gu_ex,$go_ex,$jin_ex,";
					}else{
						&K_LOG("$mmonth�� : �̹� $zname�������� 5���� ������ ��ġ�Ǿ����ϴ�.");
					}
				}
}
1;

