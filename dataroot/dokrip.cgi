
sub DOKRIP{
				$ksub2=0;
				if($zcon == 0 || $klevel < 10 || $zcon != $kcon){
					&K_LOG("�� ���ÿ����� ������ �� �����ϴ�.");
				}elsif($csub != $kpos){
					&K_LOG("�������� �ٸ��ϴ�.");
				}else{
				open(IN,"$COUNTRY_NO_LIST") or &ERR2('������ ���� �ʾҽ��ϴ�. err no :country');
				@COU_NO_DATA = <IN>;
				close(IN);
					$d_hit=0;
					foreach(@DEF_DATA){
						($mdid,$mdname,$mdtown_id,$mdtown_flg,$mdcon,$mdchara,$mdsol,$mdsub1_ex) = split(/<>/);
						if($cnum eq $mdtown_id){
							$d_hit++;
						}
					}
					if( $kclass >= 5000 && 100-$zpri-$d_hit*10 > int(rand(100))){
						foreach(@COU_DATA){
							($xcid,$xname,$xele,$xmark,$xking,$xmes,$xsub,$xpri)=split(/<>/);
							$ele{$xele} = 1;
						}
						while(){
							$rnd_max = @ELE_C-1;
							$r = int(rand($rnd_max))+1;
							if( $ele{$r} != 1 ){
								$cend = $r;
								last;
							}
						}
						$COU_NO_DATA = @COU_NO_DATA + 1;
						$kcon = $COU_NO_DATA;

						&TOWN_DATA_OPEN("$kpos");
						$zcon = $COU_NO_DATA;
						&TOWN_DATA_INPUT;

						$zcon = $COU_NO_DATA;
						push(@COU_DATA,"$COU_NO_DATA<>$cnum<>$cno<>55<>$kid<><><>1<>\n");
						open(OUT,">$COUNTRY_LIST") or &E_ERR('COUNTRY �����͸� ������ �� �����ϴ�.');
						print OUT @COU_DATA;
						close(OUT);

						push(@COU_NO_DATA,"$COU_NO_DATA<>$cnum<>$cno<>55<>$kid<><><>1<>\n");
						open(OUT,">$COUNTRY_NO_LIST") or &E_ERR('COUNTRY �����͸� ������ �� �����ϴ�.');
						print OUT @COU_NO_DATA;
						close(OUT);

						&K_LOG("$cnum���� �Ǳ��߽��ϴ�.");
						&MAP_LOG2("<font color=000088><B>[����]</B></font> $kname���� �ݶ��� ������ $zname�� �������� �� $cnum���� �Ǳ��Ͽ����ϴ�.");
						&MAP_LOG("<font color=000088><B>[����]</B></font> $kname���� �ݶ��� ������ $zname�� �������� �� $cnum���� �Ǳ��Ͽ����ϴ�.");
						&HISTORY_LOG($kid,"�ݶ��� �����Ͽ� $cnum���� �Ǳ��Ͽ����ϴ�.");
						&TOWN_CHANGE($kpos);

					}else{
						&TOWN_CHANGE($kpos);
						&BONG_DEL;
						&DELETE;
						&MAP_LOG("<font color=000088><B>[����]</B></font>$zname������ �ݶ��� �����Ͽ� $kname���� �����˷� ó���Ǿ����ϴ�.");
						$zpri -= (int(rand($zpri/20))+int(rand($zpri/20))+1);
					}
				}	
}
1;

