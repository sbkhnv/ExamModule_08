from fastapi import APIRouter
from db.database import Session, ENGINE
from db.schemas import TeamMembers
from db.models import TeamMembersModel, User
from fastapi import HTTPException, status, Depends
from fastapi.encoders import jsonable_encoder
from fastapi_jwt_auth import AuthJWT


session = Session(bind=ENGINE)

team_router = APIRouter(prefix="/team")


@team_router.get("/")
async def get_all_cities(Authentiztion: AuthJWT = Depends()):
    try:
        Authentiztion.jwt_required()

    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='unauthorized')

    check_user_token = Authentiztion.get_jwt_subject()
    check_user = session.query(User).filter(User.username == check_user_token).first()
    if check_user.is_active:
        city_list = session.query(TeamMembersModel).all()
        context = [
            {
                "id": city.id,
                "name": city.name
            }
            for city in city_list
        ]
        return jsonable_encoder(context)
    return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='unauthorized')


@team_router.get("/{id}")
async def get_all_cities(id: int, Authentiztion: AuthJWT = Depends()):
    try:
        Authentiztion.jwt_required()

    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='unauthorized')

    check_user_token = Authentiztion.get_jwt_subject()
    check_user = session.query(User).filter(User.username == check_user_token).first()
    if check_user.is_active:
        check_city = session.query(TeamMembersModel).filter(TeamMembersModel.id == id).first()
        context = [
            {
                "id": check_city.id,
                "name": check_city.name
            }
        ]
        return jsonable_encoder(context)
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='unauthorized')


@team_router.post('/create_city')
async def create_city(city: TeamMembers, Authentiztion: AuthJWT = Depends()):
    try:
        Authentiztion.jwt_required()

    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='unauthorized')

    check_user_token = Authentiztion.get_jwt_subject()
    check_user = session.query(User).filter(User.username == check_user_token).first()
    if check_user.is_superuser:
        city_check = session.query(TeamMembersModel).filter(TeamMembersModel.id == city.id).first()
        if city_check:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="City already exists")

        new_city = TeamMembersModel(
            id=city.id,
            name=city.name
        )
        session.add(new_city)
        session.commit()
        return HTTPException(status_code=status.HTTP_201_CREATED, detail="city created successfully")
    return HTTPException(status_code=status.HTTP_409_CONFLICT, detail="only admin has permission")


@team_router.put("/{id}")
async def update_city(id: int, city: TeamMembers, Authentiztion: AuthJWT = Depends()):
    try:
        Authentiztion.jwt_required()

    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='unauthorized')

    check_user_token = Authentiztion.get_jwt_subject()
    check_user = session.query(User).filter(User.username == check_user_token).first()
    if check_user.is_superuser:
        check = session.query(TeamMembersModel).filter(TeamMembersModel.id == id).first()
        check_id = session.query(TeamMembersModel).filter(TeamMembersModel.id == city.id).first()
        if check:
            if check_id is None or check_id.id == id:
                for key, value in city.dict(exclude_unset=True).items():
                    setattr(check, key, value)
                    session.commit()

                data = {
                    "code": 200,
                    "message": "update city"
                }
                return jsonable_encoder(data)

            return HTTPException(status_code=status.HTTP_409_CONFLICT, detail="yangi berilgan id da malumot mavjud!")

        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    return HTTPException(status_code=status.HTTP_409_CONFLICT, detail='only admins can update city')


@team_router.delete("/{id}")
async def delete_city(id: int, Authentiztion: AuthJWT = Depends()):
    try:
        Authentiztion.jwt_required()

    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='unauthorized')

    check_user_token = Authentiztion.get_jwt_subject()
    check_user = session.query(User).filter(User.username == check_user_token).first()
    if check_user.is_superuser:
        check = session.query(TeamMembersModel).filter(TeamMembersModel.id == id).first()
        if check:
            session.delete(check)
            session.commit()
            return HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="Deleted")

        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    return HTTPException(status_code=status.HTTP_409_CONFLICT, detail='only admins can delete city')

