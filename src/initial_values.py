import numpy as np
from typing import Tuple


def milestone_2_test_1_initial_val(lattice_grid_shape: Tuple[int, int]):
    density = np.ones(lattice_grid_shape) * 0.5
    density[lattice_grid_shape[0] / 2, lattice_grid_shape[1] / 2] = 0.6
    velocity = np.ones(lattice_grid_shape) * 0.0
    return density, velocity


def milestone_2_test_2_initial_val(lattice_grid_shape: Tuple[int, int]):
    density = np.random.uniform(0, 1, lattice_grid_shape)
    velocity = np.random.uniform(-0.1, 0.1, lattice_grid_shape + (2,))
    return density, velocity


def sinusoidal_density_x(lattice_grid_shape: Tuple[int, int], initial_p0: float, epsilon: float):
    """
    Return initial values according to p(r,0)=p_0+eps*sin(2*PI*x/lx) and u(r,0) = 0

    Args:
        lattice_grid_shape: lattice grid [lx, ly]
        initial_p0: offset
        epsilon: amplitude of swinging

    Returns:
         p(r,0)=p_0+eps*sin(2*PI*x/lx), u(r,0) = 0

    """
    assert initial_p0 + epsilon < 1, "rho can potentially be >= 1"
    assert initial_p0 - epsilon > 0, "rho can potentially be <= 0"

    x = np.arange(0, lattice_grid_shape[0])
    rho_x = initial_p0 + epsilon * np.sin(
        np.divide(
            2 * np.pi * x,
            lattice_grid_shape[0]
        )
    )
    rho = np.array(
        [rho_x for _ in range(lattice_grid_shape[1])]
    )
    rho = rho.T
    u = np.zeros(lattice_grid_shape + (2,))
    return rho, u


def sinusoidal_velocity_x(lattice_grid_shape: Tuple[int, int], epsilon: float):
    """
    Return initial values according to p(r,0)=1 and u(r,0) = eps*sin(2*PI*y/ly)

    Args:
        lattice_grid_shape: lattice grid [lx, ly]
        initial_p0: offset
        epsilon: amplitude of swinging

    Returns:
         p(r,0)=1, u(r,0) = eps*sin(2*PI*y/ly)

    """
    assert np.abs(epsilon) < 0.1, "|u| can potentially be >= 0.1"

    rho = np.ones(lattice_grid_shape)
    y = np.arange(0, lattice_grid_shape[1])
    u_y = epsilon * np.sin(
        np.divide(
            2 * np.pi * y,
            lattice_grid_shape[1]
        )
    )
    ux = np.array(
        [u_y for _ in range(lattice_grid_shape[0])]
    )
    u = np.dstack([ux, np.zeros(lattice_grid_shape)])
    return rho, u


def density_1_velocity_0_initial(lattice_grid_shape: Tuple[int, int]):
    return np.ones(lattice_grid_shape), np.zeros(lattice_grid_shape + (2,))
