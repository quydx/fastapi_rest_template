from fastapi import APIRouter

from mdpService.airflow_processor.generator import DagGenerator
from mdpService.web.api.airflow_generator.schema import BashDagRequest

router = APIRouter()


@router.post("/generate-bash")
async def generate_bash_template(item: BashDagRequest) -> str:
    """
    Generate bash template.

    @param item:
    @return:
    """
    dag_params = item.dict()
    dag_gen = DagGenerator()
    return dag_gen.generate_bash_dag(**dag_params)
