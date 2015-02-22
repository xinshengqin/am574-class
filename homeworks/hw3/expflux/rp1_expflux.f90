! =============================================================================
subroutine rp1(maxmx,meqn,mwaves,maux,mbc,mx,ql,qr,auxl,auxr,wave,s,amdq,apdq)
! =============================================================================
!
! Riemann problems for the 1D scalar equation q_t + (exp(q))_x = 0.

! waves: 1
! equations: 1

! Conserved quantities:
!       1 q
    
    implicit double precision (a-h,o-z)

    integer :: maxmx, meqn, mwaves, mbc, mx
        
    double precision :: ql(meqn,1-mbc:maxmx+mbc)
    double precision :: qr(meqn,1-mbc:maxmx+mbc)
    double precision :: s(mwaves, 1-mbc:maxmx+mbc)
    double precision :: wave(meqn, mwaves, 1-mbc:maxmx+mbc)
    double precision :: amdq(meqn, 1-mbc:maxmx+mbc)
    double precision :: apdq(meqn, 1-mbc:maxmx+mbc)
    integer :: i
 

    do i=2-mbc,mx+mbc
        wave(1,1,i) = ql(1,i) - qr(1,i-1)
        dq = qr(1,i-1) - ql(1,i)
        if (abs(dq) > 1.e-8) then
            s(1,i) = (exp(qr(1,i-1)) - exp(ql(1,i))) / dq
          else
            s(1,i) = exp(qr(1,i-1))
          endif

        ! Note that we know the speed s is always positive:
        amdq(1,i) = 0.d0
        apdq(1,i) = s(1,i) * wave(1,1,i)

        ! There cannot be transonic rarefactions, so no entropy fix needed

    enddo

    return
    end subroutine
