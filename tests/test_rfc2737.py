import os
import sys
from unittest import TestCase

import pytest
from sonic_ax_impl.mibs.ietf.rfc2737 import PhysicalTableMIBUpdater
from sonic_ax_impl.mibs.ietf.rfc2737 import FabricCardCacheUpdater

if sys.version_info.major == 3:
    from unittest import mock
else:
    import mock

modules_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(modules_path, 'src'))


class TestPhysicalTableMIBUpdater(TestCase):

    # Given: 5 physical updaters are register into reinit of PhysicalTableMIBUpdater
    # When: The first updater(XcvrCacheUpdater) raises exception in the reinit
    # Then: The remaining updaters should execute reinit without any affection,
    #       and the redis un-subscription should be called
    @mock.patch('sonic_ax_impl.mibs.ietf.rfc2737.XcvrCacheUpdater.reinit_data', side_effect=Exception('mocked error'))
    def test_PhysicalTableMIBUpdater_exception_in_reinit_data_wont_block_reinit_iteration_first(self, mocked_xcvr_reinit_data):
        updater = PhysicalTableMIBUpdater()

        with (pytest.raises(Exception) as excinfo,
              mock.patch('sonic_ax_impl.mibs.ietf.rfc2737.PsuCacheUpdater.reinit_data') as mocked_psu_reinit_data,
              mock.patch('sonic_ax_impl.mibs.ietf.rfc2737.FanDrawerCacheUpdater.reinit_data') as mocked_fan_drawer_reinit_data,
              mock.patch('sonic_ax_impl.mibs.ietf.rfc2737.FanCacheUpdater.reinit_data') as mocked_fan_cache_reinit_data,
              mock.patch('sonic_ax_impl.mibs.ietf.rfc2737.ThermalCacheUpdater.reinit_data') as mocked_thermal_reinit_data,
              mock.patch('sonic_ax_impl.mibs.ietf.rfc2737.FabricCardCacheUpdater.reinit_data') as mocked_fc_reinit_data,
              mock.patch('sonic_ax_impl.mibs.cancel_redis_pubsub') as mocked_cancel_redis_pubsub):
            updater.reinit_data()
            mocked_xcvr_reinit_data.assert_called()
            mocked_psu_reinit_data.assert_called()
            mocked_fan_drawer_reinit_data.assert_called()
            mocked_fan_cache_reinit_data.assert_called()
            mocked_thermal_reinit_data.assert_called()
            mocked_fc_reinit_data.assert_called()
            mocked_cancel_redis_pubsub.assert_called()
        assert str(excinfo.value) == "[Exception('mocked error')]"

    # Given: 5 physical updaters are register into reinit of PhysicalTableMIBUpdater
    # When: The last updater(ThermalCacheUpdater) raises exception in the reinit
    # Then: The remaining updaters should execute reinit without any affection,
    #       and the redis un-subscription should be called
    @mock.patch('sonic_ax_impl.mibs.ietf.rfc2737.ThermalCacheUpdater.reinit_data', side_effect=Exception('mocked error'))
    def test_PhysicalTableMIBUpdater_exception_in_reinit_data_wont_block_reinit_iteration_last(self, mocked_thermal_reinit_data):
        updater = PhysicalTableMIBUpdater()

        with (pytest.raises(Exception) as excinfo,
              mock.patch('sonic_ax_impl.mibs.ietf.rfc2737.XcvrCacheUpdater.reinit_data') as mocked_xcvr_reinit_data,
              mock.patch('sonic_ax_impl.mibs.ietf.rfc2737.PsuCacheUpdater.reinit_data') as mocked_psu_reinit_data,
              mock.patch(
                  'sonic_ax_impl.mibs.ietf.rfc2737.FanDrawerCacheUpdater.reinit_data') as mocked_fan_drawer_reinit_data,
              mock.patch('sonic_ax_impl.mibs.ietf.rfc2737.FabricCardCacheUpdater.reinit_data') as mocked_fc_reinit_data,
              mock.patch('sonic_ax_impl.mibs.ietf.rfc2737.FanCacheUpdater.reinit_data') as mocked_fan_cache_reinit_data,
              mock.patch('sonic_ax_impl.mibs.cancel_redis_pubsub') as mocked_cancel_redis_pubsub):
            updater.reinit_data()
            mocked_xcvr_reinit_data.assert_called()
            mocked_psu_reinit_data.assert_called()
            mocked_fan_drawer_reinit_data.assert_called()
            mocked_fan_cache_reinit_data.assert_called()
            mocked_fc_reinit_data.assert_called()
            mocked_thermal_reinit_data.assert_called()
            mocked_cancel_redis_pubsub.assert_called()
        assert str(excinfo.value) == "[Exception('mocked error')]"

    # Given: 5 physical updaters are register into reinit of PhysicalTableMIBUpdater
    # When: The first updater(XcvrCacheUpdater) raises Runtime exception in the reinit
    # Then: The remaining updaters should execute reinit without any affection,
    #       and the redis un-subscription should be called
    @mock.patch('sonic_ax_impl.mibs.ietf.rfc2737.ThermalCacheUpdater.reinit_data', side_effect=RuntimeError('mocked runtime error'))
    def test_PhysicalTableMIBUpdater_runtime_exc_in_reinit_data_wont_block_reinit_iteration_first(self, mocked_thermal_reinit_data):
        updater = PhysicalTableMIBUpdater()

        with (pytest.raises(RuntimeError) as excinfo,
              mock.patch('sonic_ax_impl.mibs.ietf.rfc2737.XcvrCacheUpdater.reinit_data') as mocked_xcvr_reinit_data,
              mock.patch('sonic_ax_impl.mibs.ietf.rfc2737.PsuCacheUpdater.reinit_data') as mocked_psu_reinit_data,
              mock.patch(
                  'sonic_ax_impl.mibs.ietf.rfc2737.FanDrawerCacheUpdater.reinit_data') as mocked_fan_drawer_reinit_data,
              mock.patch(
                  'sonic_ax_impl.mibs.ietf.rfc2737.FanCacheUpdater.reinit_data') as mocked_fan_cache_reinit_data,
              mock.patch('sonic_ax_impl.mibs.ietf.rfc2737.FabricCardCacheUpdater.reinit_data') as mocked_fc_reinit_data,
              mock.patch('sonic_ax_impl.mibs.cancel_redis_pubsub') as mocked_cancel_redis_pubsub):
            updater.reinit_data()
            mocked_thermal_reinit_data.assert_called()
            mocked_xcvr_reinit_data.assert_called()
            mocked_psu_reinit_data.assert_called()
            mocked_fan_drawer_reinit_data.assert_called()
            mocked_fan_cache_reinit_data.assert_called()
            mocked_fc_reinit_data.assert_called()
            mocked_cancel_redis_pubsub.assert_called()
        assert str(excinfo.value) == "[RuntimeError('mocked runtime error')]"

    # Given: 5 physical updaters are register into reinit of PhysicalTableMIBUpdater
    # When: The last updater(XcvrCacheUpdater) raises Runtime exception in the reinit
    # Then: The remaining updaters should execute reinit without any affection,
    #       and the redis un-subscription should be called
    @mock.patch('sonic_ax_impl.mibs.ietf.rfc2737.XcvrCacheUpdater.reinit_data', side_effect=RuntimeError('mocked runtime error'))
    def test_PhysicalTableMIBUpdater_runtime_exc_in_reinit_data_wont_block_reinit_iteration_last(self, mocked_xcvr_reinit_data):
        updater = PhysicalTableMIBUpdater()

        with (pytest.raises(RuntimeError) as exc_info,
              mock.patch('sonic_ax_impl.mibs.ietf.rfc2737.PsuCacheUpdater.reinit_data') as mocked_psu_reinit_data,
              mock.patch('sonic_ax_impl.mibs.ietf.rfc2737.FanDrawerCacheUpdater.reinit_data') as mocked_fan_drawer_reinit_data,
              mock.patch('sonic_ax_impl.mibs.ietf.rfc2737.FanCacheUpdater.reinit_data') as mocked_fan_cache_reinit_data,
              mock.patch('sonic_ax_impl.mibs.ietf.rfc2737.ThermalCacheUpdater.reinit_data') as mocked_thermal_reinit_data,
              mock.patch('sonic_ax_impl.mibs.ietf.rfc2737.FabricCardCacheUpdater.reinit_data') as mocked_fc_reinit_data,
              mock.patch('sonic_ax_impl.mibs.cancel_redis_pubsub') as mocked_cancel_redis_pubsub):
            updater.reinit_data()
            mocked_xcvr_reinit_data.assert_called()
            mocked_psu_reinit_data.assert_called()
            mocked_fan_drawer_reinit_data.assert_called()
            mocked_fan_cache_reinit_data.assert_called()
            mocked_thermal_reinit_data.assert_called()
            mocked_fc_reinit_data.assert_called()
            mocked_cancel_redis_pubsub.assert_called()
        assert str(exc_info.value) == "[RuntimeError('mocked runtime error')]"

    # Given: 5 physical updaters are register into reinit of PhysicalTableMIBUpdater
    # When: The first(XcvrCacheUpdater) and last updater(ThermalCacheUpdater)
    #       raises Runtime exception and Exception in the reinit
    # Then: The remaining updaters should execute reinit without any affection,
    #       and the redis un-subscription should be called
    #       Both the RuntimeError and Exception should be caught and combined as RuntimeError then been raised
    @mock.patch('sonic_ax_impl.mibs.ietf.rfc2737.XcvrCacheUpdater.reinit_data', side_effect=RuntimeError('mocked runtime error'))
    @mock.patch('sonic_ax_impl.mibs.ietf.rfc2737.ThermalCacheUpdater.reinit_data', side_effect=Exception('mocked error'))
    def test_PhysicalTableMIBUpdater_multi_exception(self, mocked_xcvr_reinit_data, mocked_thermal_reinit_data):
        updater = PhysicalTableMIBUpdater()

        with (pytest.raises(RuntimeError) as exc_info,
              mock.patch('sonic_ax_impl.mibs.ietf.rfc2737.PsuCacheUpdater.reinit_data') as mocked_psu_reinit_data,
              mock.patch('sonic_ax_impl.mibs.ietf.rfc2737.FanDrawerCacheUpdater.reinit_data') as mocked_fan_drawer_reinit_data,
              mock.patch('sonic_ax_impl.mibs.ietf.rfc2737.FanCacheUpdater.reinit_data') as mocked_fan_cache_reinit_data,
              mock.patch('sonic_ax_impl.mibs.ietf.rfc2737.FabricCardCacheUpdater.reinit_data') as mocked_fc_reinit_data,
              mock.patch('sonic_ax_impl.mibs.cancel_redis_pubsub') as mocked_cancel_redis_pubsub):
            updater.reinit_data()
            mocked_xcvr_reinit_data.assert_called()
            mocked_psu_reinit_data.assert_called()
            mocked_fan_drawer_reinit_data.assert_called()
            mocked_fan_cache_reinit_data.assert_called()
            mocked_fc_reinit_data.assert_called()
            mocked_thermal_reinit_data.assert_called()
            mocked_cancel_redis_pubsub.assert_called()
        assert str(exc_info.value) == "[RuntimeError('mocked runtime error'), Exception('mocked error')]"


class TestFabricCardCacheUpdater(TestCase):
    @mock.patch('sonic_ax_impl.mibs.Namespace.dbs_get_all', mock.MagicMock(return_value=({"model": "Model000", "presence": "True", "serial" : "Serial000", "is_replaceable" : "False"})))
    @mock.patch('sonic_ax_impl.mibs.ietf.rfc2737.PhysicalEntityCacheUpdater.get_physical_relation_info', mock.MagicMock(return_value=({"position_in_parent" : 0, "parent_name" : "Chassis 1"})))
    def test_update_entity_cache(self):
        updater = PhysicalTableMIBUpdater()
        fc_updater = FabricCardCacheUpdater(updater)
        update_entity_cache = getattr(fc_updater, '_update_entity_cache')

        with (mock.patch('sonic_ax_impl.mibs.ietf.rfc2737.PhysicalTableMIBUpdater.set_phy_contained_in') as mocked_phy_contained_in,
              mock.patch('sonic_ax_impl.mibs.ietf.rfc2737.PhysicalTableMIBUpdater.set_phy_fru') as mocked_set_phy_fru):
            update_entity_cache('N/A')
            mocked_phy_contained_in.assert_called()
            mocked_set_phy_fru.assert_called()
