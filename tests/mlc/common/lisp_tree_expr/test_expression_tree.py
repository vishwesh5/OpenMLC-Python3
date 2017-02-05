import unittest
import MLC.Log.log as lg
from MLC import config as config_path
from MLC.Log.log import set_logger
from MLC.mlc_parameters.mlc_parameters import Config
from MLC.Common.LispTreeExpr.LispTreeExpr import ExprException
from MLC.Common.LispTreeExpr.LispTreeExpr import LispTreeExpr
from MLC.Common.LispTreeExpr.LispTreeExpr import NotBalancedParanthesisException
from MLC.Common.LispTreeExpr.LispTreeExpr import OperationArgumentsAmountException
from MLC.Common.LispTreeExpr.LispTreeExpr import OperationNotFoundException
from MLC.Common.LispTreeExpr.LispTreeExpr import RootNotFoundExprException

import os


class ExpressionTreeTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        set_logger("testing")
        config = Config.get_instance()
        config.read(os.path.join(config_path.get_test_path(), 'mlc/individual/configuration.ini'))

    def setUp(self):
        pass

    def test_check_expression_root_not_found(self):
        expression = '123'
        self.assert_check_expression_with_exception(expression, RootNotFoundExprException)

    def test_check_expression_misplaced_parenthesis_1(self):
        expression = '(root )* 2 3))'
        self.assert_check_expression_with_exception(expression, NotBalancedParanthesisException)

    def test_check_expression_misplaced_parenthesis_2(self):
        expression = '(root (* 2 3()'
        self.assert_check_expression_with_exception(expression, NotBalancedParanthesisException)

    def test_check_expression_misplaced_parenthesis_3(self):
        expression = '(root (* 2 3)'
        self.assert_check_expression_with_exception(expression, NotBalancedParanthesisException)

    def test_check_expression_misplaced_parenthesis_4(self):
        expression = '(root (* 2 3)))'
        self.assert_check_expression_with_exception(expression, NotBalancedParanthesisException)

    def test_check_expression_operation_not_found(self):
        expression = '(root (y 2 3))'
        self.assert_check_expression_with_exception(expression, OperationNotFoundException)

    def test_check_expression_incorrect_multiply_arguments_amount(self):
        expression = '(root (* 2 3 3))'
        self.assert_check_expression_with_exception(expression, OperationArgumentsAmountException)

    def test_check_expression_incorrect_tanh_arguments_amount(self):
        expression = '(root (tanh 2 3))'
        self.assert_check_expression_with_exception(expression, OperationArgumentsAmountException)

    def test_check_expression_complex_incorrect_tanh_arguments_amount(self):
        expression = '(root (tanh 2 (* 3 (/ 2 5))))'
        self.assert_check_expression_with_exception(expression, OperationArgumentsAmountException)

    def test_check_expression_complex_incorrect_plus_arguments_amount(self):
        expression = '(root (+ (* 2 3 5) 8))'
        self.assert_check_expression_with_exception(expression, OperationArgumentsAmountException)

    def test_check_expression_simple_correct_plus_arguments_amount(self):
        expression = '(root (+ 2 3))'
        self.assert_check_expression_without_exception(expression)

    def test_check_expression_simple_correct_tanh_arguments_amount(self):
        expression = '(root (tanh 3))'
        self.assert_check_expression_without_exception(expression)

    def test_check_expression_complex_correct_plus_arguments_amount_1(self):
        expression = '(root (+ 2 (* 3 (/ 2 5))))'
        self.assert_check_expression_without_exception(expression)

    def test_check_expression_complex_correct_plus_arguments_amount_2(self):
        expression = '(root (+ 2 (* (/ 2 5) 3)))'
        self.assert_check_expression_without_exception(expression)

    def test_check_expression_complex_correct_plus_arguments_amount_3(self):
        expression = '(root (+ (* 2 3) (/ 4 5)))'
        self.assert_check_expression_without_exception(expression)

    def test_check_expression_complex_correct_plus_arguments_amount_4(self):
        expression = '(root (+ 8 (/ 4 5)))'
        self.assert_check_expression_without_exception(expression)

    def test_check_expression_complex_correct_plus_arguments_amount_5(self):
        expression = '(root (+ (* 2 3) 8))'
        self.assert_check_expression_without_exception(expression)

    def test_tree_depth_root(self):
        expression = '(root S0)'
        tree = LispTreeExpr(expression)

        # root
        root = tree.get_root_node()
        self.assertNode(root, depth=1, childs=1, expr_index=0)

        # S0
        self.assertNode(root._nodes[0], depth=1, childs=0, expr_index=6)

    def test_tree_depth_leaf(self):
        expression = '(root (tanh S0))'
        tree = LispTreeExpr(expression)

        # root
        root = tree.get_root_node()
        self.assertNode(root, depth=1, childs=1, expr_index=0)

        # (tanh S0)
        sub_expression = root._nodes[0]
        self.assertNode(sub_expression, depth=2, childs=1, expr_index=6)

        # S0
        self.assertNode(sub_expression._nodes[0], depth=2, childs=0, expr_index=12)

    def test_tree_subtree(self):
        expression = '(root (+ (tanh S0) (cos S1))))'
        tree = LispTreeExpr(expression)

        # root
        root = tree.get_root_node()
        self.assertNode(root, 1, 1, expr_index=0)

        # (+ (tanh S0) (cos S1)))
        sum_node = root._nodes[0]
        self.assertNode(sum_node, depth=2, childs=2, expr_index=6)

        # (tanh S0)
        subtree_0 = sum_node._nodes[0]
        self.assertNode(subtree_0, depth=3, childs=1, expr_index=9)
        self.assertNode(subtree_0._nodes[0], depth=3, childs=0, expr_index=15)

        # (cos S1)
        subtree_1 = sum_node._nodes[1]
        self.assertNode(subtree_1, depth=3, childs=1, expr_index=19)
        self.assertNode(subtree_1._nodes[0], depth=3, childs=0, expr_index=24)

    def assertNode(self, node, depth, childs, expr_index):
        self.assertEquals(node.get_depth(), depth)
        self.assertEquals(node.get_expr_index(), expr_index)

        if not node.is_leaf():
            self.assertEquals(len(node._nodes), childs)

    def assert_check_expression_with_exception(self, expression, exception_class):
        try:
            LispTreeExpr.check_expression(expression)
            self.assertTrue(True, False)
        except exception_class:
            self.assertTrue(True, True)

    def assert_check_expression_without_exception(self, expression):
        try:
            LispTreeExpr.check_expression(expression)
            self.assertTrue(True, True)
        except ExprException:
            self.assertTrue(True, False)
