import logging
from Creation.CreationFactory import CreationFactory


class Population(object):
    def __init__(self, eng, config, gen=None):
        self._eng = eng
        self._config = config

        if gen:
            self._gen = gen

        cascade = config.get_param('OPTIMIZATION', 'cascade', type='array')
        size = config.get_param('POPULATION', 'size', type='array')

        self._gen = 1 if cascade[1] == 0 else cascade[1]
        self._gen_size = cascade[1] \
            if (self._gen > 1 and len(size) > 1) else size[0]
        self._state = 'init'

        logging.getLogger("default").debug("Population created. Number: " +
                                           str(self._gen) + " - Size: " +
                                           str(self._gen_size))

    def create(self):
        gen_method = self._config.get_param('GP', 'generation_method')
        logging.info("Using " + gen_method + " to generate population")
        gen_creator = CreationFactory.make(self._eng, self._config, gen_method)
        gen_creator.create(self._gen_size)
