#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include "validation.h"

namespace py = pybind11;

PYBIND11_MODULE(bitcoinkernel, m) {
    m.doc() = "Python bindings for libbitcoinkernel";

    m.def("MainNetParams", CChainParams::Main);
    m.def("TestNetParams", CChainParams::TestNet);

    py::class_<BlockValidationState>(m, "BlockValidationState")
        .def(py::init<>())
        .def("IsValid", &BlockValidationState::IsValid)
        .def("IsError", &BlockValidationState::IsError)
        .def("GetRejectReason", &BlockValidationState::GetRejectReason);
        ;

    py::class_<CChainParams>(m, "CChainParams")
        .def("GetChainTypeString", &CChainParams::GetChainTypeString)
        ;
}
