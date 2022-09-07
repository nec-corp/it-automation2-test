#   Copyright 2022 NEC Corporation
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import connexion

from common_libs.common import *  # noqa: F403
from common_libs.api import api_filter
from libs.organization_common import check_menu_info, check_auth_menu, check_sheet_type
from libs import driver_controll

@api_filter
def get_driver_execute_data(organization_id, workspace_id, menu, execution_no):  # noqa: E501
    """get_driver_execute_data

    Driver作業実行の状態取得 # noqa: E501

    :param organization_id: OrganizationID
    :type organization_id: str
    :param workspace_id: WorkspaceID
    :type workspace_id: str
    :param menu: メニュー名
    :type menu: str
    :param execution_no: 実行No
    :type execution_no: str

    :rtype: InlineResponse20011
    """

    # DB接続
    objdbca = DBConnectWs(workspace_id)  # noqa: F405
    
    # メニューの存在確認
    check_menu_info(menu, objdbca)

    # 『メニュー-テーブル紐付管理』の取得とシートタイプのチェック
    sheet_type_list = ['12']
    check_sheet_type(menu, sheet_type_list, objdbca)

    # メニューに対するロール権限をチェック
    check_auth_menu(menu, objdbca)
    
    return 'do some magic!',


@api_filter
def get_driver_execute_info(organization_id, workspace_id, menu):  # noqa: E501
    """get_driver_execute_info

    Movement,Operationのメニューの基本情報および項目情報を取得する # noqa: E501

    :param organization_id: OrganizationID
    :type organization_id: str
    :param workspace_id: WorkspaceID
    :type workspace_id: str
    :param menu: メニュー名
    :type menu: str

    :rtype: InlineResponse20018
    """

    # DB接続
    objdbca = DBConnectWs(workspace_id)  # noqa: F405
    
    # メニューの存在確認
    check_menu_info(menu, objdbca)

    # 『メニュー-テーブル紐付管理』の取得とシートタイプのチェック
    sheet_type_list = ['11']
    check_sheet_type(menu, sheet_type_list, objdbca)

    # メニューに対するロール権限をチェック
    check_auth_menu(menu, objdbca)
    
    # 作業実行メニューとMovement一覧の対応
    movement_target = {'execution_ansible_role': 'movement_list_ansible_role'}

    # 作業実行関連のメニューの基本情報および項目情報の取得
    target_menus = ["operation_list", movement_target[menu]]
    data = {}
    for target in target_menus:
        data[target] = menu_info.collect_menu_info(objdbca, target)

    return data,


@api_filter
def get_driver_execute_search_candidates(organization_id, workspace_id, menu, target, column):  # noqa: E501
    """get_driver_execute_search_candidates

    表示フィルタで利用するプルダウン検索の候補一覧を取得する # noqa: E501

    :param organization_id: OrganizationID
    :type organization_id: str
    :param workspace_id: WorkspaceID
    :type workspace_id: str
    :param menu: メニュー名
    :type menu: str
    :param target: movement_list or operation_list
    :type target: str
    :param column: REST用項目名
    :type column: str

    :rtype: InlineResponse2003
    """

    # DB接続
    objdbca = DBConnectWs(workspace_id)  # noqa: F405
    
    # メニューの存在確認
    check_menu_info(menu, objdbca)

    # 『メニュー-テーブル紐付管理』の取得とシートタイプのチェック
    sheet_type_list = ['11']
    check_sheet_type(menu, sheet_type_list, objdbca)

    # メニューに対するロール権限をチェック
    check_auth_menu(menu, objdbca)
    
    # 作業実行メニューとMovement一覧の対応
    movement_target = {'execution_ansible_role': 'movement_list_ansible_role'}

    # targetのチェック
    target_menus = ["operation_list", movement_target[menu]]
    if target not in target_menus:
        log_msg_args = []
        api_msg_args = []
        raise AppException("499-00008", log_msg_args, api_msg_args)  # noqa: F405

    # 対象項目のプルダウン検索候補一覧を取得
    data = menu_info.collect_search_candidates(objdbca, target, column)
    return data,


@api_filter
def post_driver_cancel(organization_id, workspace_id, menu, execution_no):  # noqa: E501
    """post_driver_cancel

    Driver作業実行の予約取消 # noqa: E501

    :param organization_id: OrganizationID
    :type organization_id: str
    :param workspace_id: WorkspaceID
    :type workspace_id: str
    :param menu: メニュー名
    :type menu: str
    :param execution_no: 実行No
    :type execution_no: str

    :rtype: InlineResponse20011
    """

    # DB接続
    objdbca = DBConnectWs(workspace_id)  # noqa: F405
    
    # メニューの存在確認
    check_menu_info(menu, objdbca)

    # 『メニュー-テーブル紐付管理』の取得とシートタイプのチェック
    sheet_type_list = ['12']
    check_sheet_type(menu, sheet_type_list, objdbca)

    # メニューに対するロール権限をチェック
    check_auth_menu(menu, objdbca)
    
    return 'do some magic!',

@api_filter
def post_driver_excecute(organization_id, workspace_id, menu, body=None):  # noqa: E501
    """post_driver_excecute

    Driver作業実行 # noqa: E501

    :param organization_id: OrganizationID
    :type organization_id: str
    :param workspace_id: WorkspaceID
    :type workspace_id: str
    :param menu: メニュー名
    :type menu: str
    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse20017
    """

    # DB接続
    objdbca = DBConnectWs(workspace_id)  # noqa: F405
    
    # メニューの存在確認
    check_menu_info(menu, objdbca)

    # 『メニュー-テーブル紐付管理』の取得とシートタイプのチェック
    sheet_type_list = ['11']
    check_sheet_type(menu, sheet_type_list, objdbca)

    # メニューに対するロール権限をチェック
    check_auth_menu(menu, objdbca)
    
    parameter = {}
    if connexion.request.is_json:
        body = dict(connexion.request.get_json())
        parameter = body

    # 作業管理に登録
    result = driver_controll.insert_execution_list(objdbca, menu, parameter, 'execute')

    return result,


@api_filter
def post_driver_execute_check_parameter(organization_id, workspace_id, menu, body=None):  # noqa: E501
    """post_driver_execute_check_parameter

    Driver作業実行(実行時に使用するパラメータ確認) # noqa: E501

    :param organization_id: OrganizationID
    :type organization_id: str
    :param workspace_id: WorkspaceID
    :type workspace_id: str
    :param menu: メニュー名
    :type menu: str
    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse20017
    """

    # DB接続
    objdbca = DBConnectWs(workspace_id)  # noqa: F405
    
    # メニューの存在確認
    check_menu_info(menu, objdbca)

    # 『メニュー-テーブル紐付管理』の取得とシートタイプのチェック
    sheet_type_list = ['11']
    check_sheet_type(menu, sheet_type_list, objdbca)

    # メニューに対するロール権限をチェック
    check_auth_menu(menu, objdbca)
    
    parameter = {}
    if connexion.request.is_json:
        body = dict(connexion.request.get_json())
        parameter = body

    # 作業管理に登録
    result = driver_controll.insert_execution_list(objdbca, menu, parameter, 'check_parameter')

    return result,


@api_filter
def post_driver_execute_dry_run(organization_id, workspace_id, menu, body=None):  # noqa: E501
    """post_driver_execute_dry_run

    Driver作業実行（ドライラン）&lt;/br&gt; AnsibleDriverの場合はDryRun、TerraformDriverの場合はPlanのみの実行を行う  # noqa: E501

    :param organization_id: OrganizationID
    :type organization_id: str
    :param workspace_id: WorkspaceID
    :type workspace_id: str
    :param menu: メニュー名
    :type menu: str
    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse20017
    """

    # DB接続
    objdbca = DBConnectWs(workspace_id)  # noqa: F405
    
    # メニューの存在確認
    check_menu_info(menu, objdbca)

    # 『メニュー-テーブル紐付管理』の取得とシートタイプのチェック
    sheet_type_list = ['11']
    check_sheet_type(menu, sheet_type_list, objdbca)

    # メニューに対するロール権限をチェック
    check_auth_menu(menu, objdbca)
    
    parameter = {}
    if connexion.request.is_json:
        body = dict(connexion.request.get_json())
        parameter = body

    # 作業管理に登録
    result = driver_controll.insert_execution_list(objdbca, menu, parameter, 'dry_run')

    return result,


@api_filter
def post_driver_execute_filter(organization_id, workspace_id, menu, target, body=None):  # noqa: E501
    """post_driver_execute_filter

    Movement,Operationを対象に、検索条件を指定し、レコードを取得する # noqa: E501

    :param organization_id: OrganizationID
    :type organization_id: str
    :param workspace_id: WorkspaceID
    :type workspace_id: str
    :param menu: メニュー名
    :type menu: str
    :param target: movement_list or operation_list
    :type target: str
    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse2005
    """

    # DB接続
    objdbca = DBConnectWs(workspace_id)  # noqa: F405

    # メニューの存在確認
    check_menu_info(menu, objdbca)

    # 『メニュー-テーブル紐付管理』の取得とシートタイプのチェック
    sheet_type_list = ['11']
    check_sheet_type(menu, sheet_type_list, objdbca)

    # メニューに対するロール権限をチェック
    check_auth_menu(menu, objdbca)
    
    # 作業実行メニューとMovement一覧の対応
    movement_target = {'execution_ansible_role': 'movement_list_ansible_role'}

    # targetのチェック
    target_menus = ["operation_list", movement_target[menu]]
    if target not in target_menus:
        log_msg_args = []
        api_msg_args = []
        raise AppException("499-00008", log_msg_args, api_msg_args)  # noqa: F405
    
    filter_parameter = {}
    if connexion.request.is_json:
        body = dict(connexion.request.get_json())
        filter_parameter = body
        
    # メニューのカラム情報を取得
    result_data = menu_filter.rest_filter(objdbca, target, filter_parameter)
    return result_data,


@api_filter
def post_driver_scram(organization_id, workspace_id, menu, execution_no):  # noqa: E501
    """post_driver_scram

    Driver作業実行の緊急停止 # noqa: E501

    :param organization_id: OrganizationID
    :type organization_id: str
    :param workspace_id: WorkspaceID
    :type workspace_id: str
    :param menu: メニュー名
    :type menu: str
    :param execution_no: 実行No
    :type execution_no: str

    :rtype: InlineResponse20011
    """

    # DB接続
    objdbca = DBConnectWs(workspace_id)  # noqa: F405
    
    # メニューの存在確認
    check_menu_info(menu, objdbca)

    # 『メニュー-テーブル紐付管理』の取得とシートタイプのチェック
    sheet_type_list = ['12']
    check_sheet_type(menu, sheet_type_list, objdbca)

    # メニューに対するロール権限をチェック
    check_auth_menu(menu, objdbca)
    
    return 'do some magic!',
