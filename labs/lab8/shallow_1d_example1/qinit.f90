subroutine qinit(meqn,mbc,mx,xlower,dx,q,maux,aux)

    ! Set initial conditions for the q array.

    implicit none
    
    integer, intent(in) :: meqn,mbc,mx,maux
    real(kind=8), intent(in) :: xlower,dx
    real(kind=8), intent(in) :: aux(maux,1-mbc:mx+mbc)
    real(kind=8), intent(inout) :: q(meqn,1-mbc:mx+mbc)

    integer :: i
    real(kind=8) :: beta, xcell
    common /cqinit/ beta
 
 
      do i=1,mx
         xcell = xlower + (i-0.5d0)*dx
         q(1,i) = 1.d0 + 0.9d0*dexp(-beta * (xcell-1.d0)**2)  
         q(2,i) = 0.d0
      enddo

end subroutine qinit

