import sys
import MLC.Log.log as lg

from MLC.matlab_engine import MatlabEngine
from MLC.mlc_parameters.mlc_parameters import Config
from MLC.mlc_table.MLCTable import MLCTable


class StandaloneEvaluator(object):

    def __init__(self, callback):
        self._eng = MatlabEngine.engine()
        self._config = Config.get_instance()
        self._callback = callback

    def evaluate(self, indivs):
        jj = []

        lg.logger_.info("Evaluating %s individuals" % len(indivs))

        for index in indivs:
            lg.logger_.debug('[POP][STAND_EVAL] Individual N#' + str(index))

            # Retrieve the individual to be evaluated
            py_indiv = MLCTable.get_instance().get_individual(index)
            lg.logger_.debug('[POP][STAND_EVAL] Individual N#' + str(index) +
                             ' Value: ' + py_indiv.get_value())

            try:
                jj.append(self._callback.cost(py_indiv))
            except KeyError:
                lg.logger_.error("[POP][STAND_EVAL] Evaluation Function " +
                                 "doesn't exists. Aborting progam.")
                sys.exit(-1)

        return jj
