from myScript import load_first_posts
from botcity.maestro import *
from botcity.core import DesktopBot  # If using BotCity desktop automation


def main():
    maestro = BotMaestroSDK.from_sys_args()
    maestro.task_id = 1
    maestro.login(
        server="https://developers.botcity.dev",
        login="a87e9b61-eeec-4d49-b5a7-0033f69327a8",
        key="A87_R1OWVNVAKLL6NNK4BIFD"
    )
    # execution = maestro.get_execution()

    # your automation logic here...
    total, success, failed = load_first_posts(1)
    # Finish task reporting

    try:
        maestro = BotMaestroSDK.from_sys_args()
        execution = maestro.get_execution()
        task_id = execution.task_id

        maestro.finish_task(
            task_id=task_id,
            status=AutomationTaskFinishStatus.SUCCESS,
            message="Finished successfully",
            total_items=total,
            processed_items=success,
            failed_items=failed
        )
    except Exception as e:
        print(" Not running in Maestro — skipping finish_task.")


if __name__ == "__main__":
    main()
