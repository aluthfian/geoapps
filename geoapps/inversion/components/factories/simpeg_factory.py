#  Copyright (c) 2023 Mira Geoscience Ltd.
#
#  This file is part of geoapps.
#
#  geoapps is distributed under the terms and conditions of the MIT License
#  (see LICENSE file at the root of this source code package).

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from geoapps.driver_base.params import BaseParams

# TODO Redesign simpeg factory to avoid pylint arguments-differ complaint


class SimPEGFactory:
    """
    Build SimPEG objects based on inversion type.

    Parameters
    ----------
    params :
        Driver parameters object.
    factory_type :
        Concrete factory type.
    simpeg_object :
        Abstract SimPEG object.

    Methods
    -------
    assemble_arguments():
        Assemble arguments for SimPEG object instantiation.
    assemble_keyword_arguments():
        Assemble keyword arguments for SimPEG object instantiation.
    build():
        Generate SimPEG object with assembled arguments and keyword arguments.
    """

    valid_factory_types = [
        "gravity",
        "magnetic scalar",
        "magnetic vector",
        "direct current 3d",
        "direct current 2d",
        "induced polarization 3d",
        "induced polarization 2d",
        "magnetotellurics",
        "tipper",
    ]

    def __init__(self, params: BaseParams):
        """
        :param params: Driver parameters object.
        :param factory_type: Concrete factory type.
        :param simpeg_object: Abstract SimPEG object.

        """
        self.params = params
        self.factory_type: str = params.inversion_type
        self.simpeg_object = None

    @property
    def factory_type(self):
        return self._factory_type

    @factory_type.setter
    def factory_type(self, val):
        if val not in self.valid_factory_types:
            msg = f"Factory type: {val} not implemented yet."
            raise NotImplementedError(msg)
        else:
            self._factory_type = val

    def concrete_object(self):
        """To be over-ridden in factory implementations."""

    def assemble_arguments(self, **kwargs):  # pylint: disable=unused-argument
        """To be over-ridden in factory implementations."""
        return []

    def assemble_keyword_arguments(self, **kwargs):  # pylint: disable=unused-argument
        """To be over-ridden in factory implementations."""
        return {}

    def build(self, **kwargs):
        """To be over-ridden in factory implementations."""

        class_args = self.assemble_arguments(**kwargs)
        class_kwargs = self.assemble_keyword_arguments(**kwargs)
        return self.simpeg_object(  # pylint: disable=not-callable
            *class_args, **class_kwargs
        )
